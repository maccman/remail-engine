import logging, yaml
from django.utils import simplejson as json
from google.appengine.ext import webapp
from google.appengine.api import mail

settings = yaml.load(open('settings.yaml'))

def safe_dict(d): 
  """
    Recursively clone json structure with UTF-8 dictionary keys
    http://bugs.python.org/issue2646
  """ 
  if isinstance(d, dict): 
    return dict([(k.encode('utf-8'), safe_dict(v)) for k,v in d.iteritems()]) 
  elif isinstance(d, list): 
    return [safe_dict(x) for x in d] 
  else: 
    return d

class OutboundHandler(webapp.RequestHandler):

  def post(self, *args):
    api_key = self.request.headers.get('Authorization')
    
    if api_key != settings['api_key']:
      logging.error("Invalid API key: " + api_key)
      self.error(401)
      return
    
    body  = self.request.body
    email = json.loads(body)
    mail.EmailMessage(**safe_dict(email)).send()