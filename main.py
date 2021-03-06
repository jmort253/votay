import wsgiref.handlers
from google.appengine.ext import webapp
from google.appengine.ext import db
from google.appengine.api import users
from google.appengine.ext.webapp import template
import os
import sys

class MainHandler(webapp.RequestHandler):
  def get(self,path):
    self.response.headers['Content-Type'] = 'text/plain'
    self.response.out.write('User-agent: *\n')
    self.response.out.write('Sitemap: http://www.votay.com/sitemap.xml')
    
def main():
  application = webapp.WSGIApplication([('/(.*)', MainHandler)
                                        ],
                                       debug=True)
  wsgiref.handlers.CGIHandler().run(application)


if __name__ == '__main__':
  main()
