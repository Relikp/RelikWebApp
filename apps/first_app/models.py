from __future__ import unicode_literals
from django.db import models
import re
import bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class userManager(models.Manager):
      def basic_validator(self, postData):
            errors = {}
            if len(postData['first_name']) < 2:
                  errors["name"] = "Name should be at least 2 characters"
            if len(postData['last_name']) < 2:
                  errors["name"] = "Last name should be at least 2 characters"
            if len(postData['email']) < 1:
                  errors["desc"] = "Must include email"
            matching_users = user.objects.filter(email = postData["email"])
            if len(matching_users) != 0:
                  errors["Register_again"] = "This user already exists"
            if not EMAIL_REGEX.match(postData['email']):
                  errors["email"] = "Please enter a valid email"
            if len(postData['password']) < 8:
                  errors["password"] = "Must be at least 8 characters email"
            if postData['password'] != postData['conf_password']:
                  errors["desc"] = "Passwords do not match"
            return errors

      def login_validator(self, postData):
            errors = {}
            matching_users = user.objects.filter(email = postData["email"])
            if len(matching_users) == 0:
                  errors["no user"] = "login failed"
            else:
                  matching_user = matching_users[0]
                  if bcrypt.checkpw(postData["password"].encode(), matching_user.password.encode()):
                        print("Passwords match")
                  else:
                        errors["login"] = "login failed"
            return errors      


class user(models.Model):
      first_name = models.CharField(max_length=255)
      last_name = models.CharField(max_length=255)
      email = models.CharField(max_length=255)
      password = models.CharField(max_length=255)
      created_at = models.DateTimeField(auto_now_add = True)
      updated_at = models.DateTimeField(auto_now = True)

      objects = userManager()

