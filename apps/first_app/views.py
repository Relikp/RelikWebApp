from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
from . models import *
from django.contrib import messages
  

def index(request):
	request.session["name"] = ""
	request.session["alias"] = ""
	request.session["email"] = ""
	return render (request, "login_and_registration/index.html")
 
def add_user(request):
	request.session["name"] = request.POST["name"]
	request.session["alias"] = request.POST["alias"]
	request.session["email"] = request.POST["email"]
	errors = user.objects.basic_validator(request.POST)
	if len(errors):
		for key, value in errors.items():
			messages.error(request, value)
		return redirect("/back_to_registration")
	else:
		password = request.POST["password"]
		pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
		user_to_add = user.objects.create()
		user_to_add.name = request.POST["name"]
		user_to_add.alias = request.POST["alias"]
		user_to_add.email = request.POST["email"]
		user_to_add.password = pw
		user_to_add.save()
		current_user = user.objects.get(alias = request.POST["alias"])
		request.session["user_id"] = current_user.id
		request.session["name"] = ""
		request.session["email"] = ""
		return redirect('/quotes')

def back_to_registration(request):
 	return render (request, "login_and_registration/index.html")

def login(request):
	if request.method == "POST":
		errors = user.objects.login_validator(request.POST)
		if len(errors):
			for key, value in errors.items():
				messages.error(request, value)
			return redirect("/")
		else:
			current_user = user.objects.get(email = request.POST["email"])
			request.session["user_id"] = current_user.id
			request.session["alias"] = current_user.alias
			return redirect('/quotes')	
	return redirect("/")

def quotes(request):
	current_user = user.objects.get(id=request.session["user_id"])
	user_quote_list = quote.objects.filter(liked_by=current_user).order_by("-created_at")
	others_favorites = quote.objects.exclude(liked_by=current_user).order_by("-created_at")
	context = {	
		"user_quote_list" : user_quote_list,
		"others_favorites" : others_favorites,
	}
	return render (request, "login_and_registration/user_quotes_page.html", context)

def logout(request):
	request.session["alias"] = ""
	request.session["user_is"] = ""
	return redirect ("/")

def add_quote(request):
	if request.method == "POST":	
		errors = user.objects.new_quote_validator(request.POST) 
		if len(errors):
			for key, value in errors.items():
				messages.error(request, value)
			return redirect("/quotes")
		else:
			# Identifies the current user
			current_user = user.objects.get(id=request.session["user_id"])
			# Identifies the quote to add and its attributes
			a = quote.objects.create(message=request.POST["new_quote"], speaker=request.POST["speaker"], created_by=current_user)
			# Adds the quoter (many-to-many relationship) and executes
			a.liked_by.add(current_user)
			# Save
			a.save()
			return redirect('/quotes') 

def remove_quote(request, id):
	current_user = user.objects.get(id=request.session["user_id"])
	quote_to_remove = current_user.liked_quotes.get(id=id)
	current_user.liked_quotes.remove(quote_to_remove)
	return redirect ('/quotes')

def destroy(request, id):
	product_to_destroy = item.objects.get(id=id)
	product_to_destroy.delete()
	return redirect ('/dashboard')

def user_info(request, id):
	user_to_be_presented = user.objects.get(id=id)
	user_quotes_to_show = quote.objects.filter(created_by=user_to_be_presented)
	count = len(user_quotes_to_show)
	context = {
		"user_to_be_presented": user_to_be_presented,
		"user_quotes_to_show": user_quotes_to_show,
		"count": count
	}
	return render (request, "login_and_registration/user_info.html", context)

def liked_quote(request, id):
	current_user = user.objects.get(alias=request.session['alias'])
	quote_to_add = quote.objects.get(id=id)
	current_user.liked_quotes.add(quote_to_add)
	return redirect ('/quotes')

		
def liked_quote(request, id):
	current_user = user.objects.get(alias=request.session['alias'])
	quote_to_add = quote.objects.get(id=id)
	current_user.liked_quotes.add(quote_to_add)
	return redirect ('/quotes')



