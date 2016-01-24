import webapp2
import json
import os
from google.appengine.ext.webapp import template

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello, World!')

class InputPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello, World2!')
        test=self.request.params['test']
        self.response.write(test)

    def post(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello, World2!')
        body= json.loads(self.request.body)
        test=body['test']
        self.response.write(test)

class DisplayPage(webapp2.RequestHandler):
    def get(self):

        path = os.path.join(os.path.dirname(__file__), 'index.html')
        template_values = {
            'greetings': 'Hello',
            'url': 'url',
            'url_linktext': 'linkeytext',
        }
        self.response.out.write(template.render(path, template_values))

app = webapp2.WSGIApplication([
    (r'/', MainPage),
    (r'/in/*',InputPage),
    (r'/display', DisplayPage),
], debug=True)