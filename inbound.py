import logging, email, yaml
from django.utils import simplejson as json
from google.appengine.ext import webapp 
from google.appengine.ext.webapp.mail_handlers import InboundMailHandler
from google.appengine.api.urlfetch import fetch

config = yaml.load(open('settings.yaml'))

class LogSenderHandler(InboundMailHandler):
    def receive(self, message):
        logging.info("Received a message from: " + message.sender)
        result = {'email': {'raw': message.original}}
        fetch(config['outbound_url'], payload=json.dumps(result), method="POST")