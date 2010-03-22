import logging, email, yaml
from django.utils import simplejson as json
from google.appengine.ext import webapp, deferred
from google.appengine.ext.webapp.mail_handlers import InboundMailHandler
from google.appengine.api.urlfetch import fetch

settings = yaml.load(open('settings.yaml'))

def callback(raw):
  result = {'email': {'raw': raw}}
  
  fetch(settings['outbound_url'], 
        payload=json.dumps(result), 
        method="POST", 
        headers={
          'Authorization': settings['api_key'],
          'Content-Type': 'application/json'
        }
       )

class InboundHandler(InboundMailHandler):
    def receive(self, message):
      logging.info("Received a message from: " + message.sender)
      deferred.defer(callback, message.original.as_string(True), _queue='inbound')