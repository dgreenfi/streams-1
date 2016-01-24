import webapp2
import json
import os
from google.appengine.ext.webapp import template
from google.appengine.ext import ndb
from model import TestData
import random
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
        data=['1','2','Hello']
        data = TestData.query_test().fetch(20)
        print data
        data=[d.content for d in data]

        template_values = {
            'greetings': data,
            'url': 'url',
            'url_linktext': 'linkeytext',
        }
        self.response.out.write(template.render(path, template_values))
        #greeting = Greeting(parent=ndb.Key("Book",
        #                                   guestbook_name or "*notitle*"),
        #                    content=self.request.get('content'))

        #need to read key docs
        test = TestData()
        #test.key= ndb.Key(TestData)
        num= str(random.randint(1, 100))
        test.content="Hello my friend "+ num
        test.put()

app = webapp2.WSGIApplication([
    (r'/', MainPage),
    (r'/in/*',InputPage),
    (r'/display', DisplayPage),
], debug=True)