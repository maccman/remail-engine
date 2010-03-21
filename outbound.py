import yaml
from django.utils import simplejson as json
from google.appengine.ext import webapp
from google.appengine.api import mail

config = yaml.load(open('settings.yaml'))

class OutboundHandler(webapp.RequestHandler):

  def post(self):
    api_key = request.headers.get('Authorization')
    if api_key != config['api_key']:
      self.error(401)
      return
    
    data = self.request.get('data')
    email = json.loads(data)
    email = obj['email']
    mail.EmailMessage(**email).send()