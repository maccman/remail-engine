from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from outbound import OutboundHandler

def main():
  application = webapp.WSGIApplication([('/emails(\.json)*', OutboundHandler)],
                                       debug=True)
  util.run_wsgi_app(application)


if __name__ == '__main__':
  main()
