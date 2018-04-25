from __future__ import unicode_literals
from django.db import models
import re
import bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class userManager(models.Manager):
      def basic_validator(self, postData):
            errors = {}
            if len(postData['name']) < 3:
                  errors["name"] = "Name should be at least 3 characters"
            if len(postData['alias']) < 3:
                  errors["name"] = "Alias should be at least 3 characters"
            if len(postData['email']) < 1:
                  errors["desc"] = "Must include email"
            matching_users = user.objects.filter(email = postData["email"])
            if len(matching_users) != 0:
                  errors["Register_again"] = "This user already exists"
            if len(postData['password']) < 8:
                  errors["password"] = "Must be at least 8 characters email"
            if postData['password'] != postData['conf_password']:
                  errors["desc"] = "Passwords do not match"
            return errors

      def login_validator(self, postData):
            errors = {}
            print("STATION 1")
            matching_users = user.objects.filter(email = postData["email"])
            print("STATION 2")
            if len(matching_users) == 0:
                  errors["no user"] = "login failed"
            else:
                  matching_user = matching_users[0]
                  if bcrypt.checkpw(postData["password"].encode(), matching_user.password.encode()):
                        print("Passwords match")
                  else:
                        errors["login"] = "login failed"
            return errors      

      def new_quote_validator(self, postData):
            errors = {}
            matching_quote = quote.objects.filter(message = postData["new_quote"])
            if len(postData["speaker"]) < 4:
                  errors["non valid speaker"] = "Please enter valid name"
            if len(postData["new_quote"]) < 11:
                  errors["non valid quote"] = "Please enter longer quote"
            return errors      

class user(models.Model):
      name = models.CharField(max_length=255)
      alias = models.CharField(max_length=255)
      email = models.CharField(max_length=255)
      password = models.CharField(max_length=255)
      created_at = models.DateTimeField(auto_now_add = True)
      updated_at = models.DateTimeField(auto_now = True)
      objects = userManager()

class quote(models.Model):
      message = models.CharField(max_length=255)
      speaker = models.CharField(max_length=255)
      created_at = models.DateTimeField(auto_now_add = True)
      updated_at = models.DateTimeField(auto_now = True)
      created_by = models.ForeignKey(user, related_name="created_quote")
      liked_by = models.ManyToManyField(user, related_name="liked_quotes")
      objects = userManager()


