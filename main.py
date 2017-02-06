#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import os
import jinja2
from input_verification import *
template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader= jinja2.FileSystemLoader(template_dir), autoescape=True, auto_reload=True)


class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        print(template, kw)
        self.write(self.render_str(template, **kw))


class MainPage(Handler):
    def get(self):
        self.render("sign_up_form.html")


class SubmitHandler(Handler):
    def get(self, **kwargs):
        self.render("sign_up_form.html", username_error=" Invalid username.")
        #return self.render("sign_up_form.html", parameter=parameter_value)

    def post(self):

        username = self.request.get("username")
        if not valid_username(username):
            return self.render("sign_up_form.html", username_error=" Invalid username.")


        password = self.request.get("password")
        if not valid_password(password):
            return self.render("sign_up_form.html", password_error=" Invalid password.")


        password_verification =  self.request.get("verify")
        if not verify_password(password, password_verification):
            return self.render("sign_up_form.html", password_error=" Password's do not match.")


        email = self.request.get("email")
        if len(email) != 0:
            if not valid_email(email):
                return self.render("sign_up_form.html", email_error=" Invalid email")

        return self.render("success_page.html", username=username)


class FizzBuzzHandler(Handler):
    def get(self):
        n = self.request.get('n', 0)
        n = n and int(n)
        self.render('fizzbuzz.html', n=n)


app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/fizzbuzz', FizzBuzzHandler),
    ('/submit', SubmitHandler)
], debug=True)
