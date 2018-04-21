from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
from .models import *
from django.contrib import messages
  

def index(request):
	request.session["FirstName"] = ""
	request.session["LastName"] = ""
	request.session["Email"] = ""
	return render (request, "login_and_registration/index.html")
 
def add_user(request):
	request.session["FirstName"] = request.POST["first_name"]
	request.session["LastName"] = request.POST["last_name"]
	request.session["Email"] = request.POST["email"]
	# pass the post data to the method we wrote and save the response in a variable called errors
	errors = user.objects.basic_validator(request.POST)
	# check if the errors object has anything in it
	if len(errors):
		# if the errors object contains anything, loop through each key-value pair and make a flash message
		for key, value in errors.items():
			messages.error(request, value)
		# redirect the user back to the form to fix the errors
		return redirect("/back_to_registration")
	else:
		password = request.POST["password"]
		pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
		user.objects.create(first_name=request.POST["first_name"], last_name=request.POST["last_name"], email=request.POST["email"], password=pw)
		request.session["FirstName"] = ""
		request.session["LastName"] = ""
		request.session["Email"] = ""
		return redirect('/success')

def login(request):
	if request.method == "POST":
		# pass the post data to the method we wrote and save the response in a variable called errors
		errors = user.objects.login_validator(request.POST)
		# check if the errors object has anything in it
		if len(errors):
			# if the errors object contains anything, loop through each key-value pair and make a flash message
			for key, value in errors.items():
				messages.error(request, value)
			# redirect the user back to the form to fix the errors
			return redirect("/")
		else:
			return redirect('/success')	
	return redirect("/")

def success(request):
 	return render (request, "login_and_registration/success.html")

def back_to_registration(request):
 	return render (request, "login_and_registration/index.html")