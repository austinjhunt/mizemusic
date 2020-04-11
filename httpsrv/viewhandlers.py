from .models import *
from .util import * 
from django.shortcuts import render
import json,requests
from django.db.models import Q
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime,timedelta
from django.forms.models import model_to_dict


def index_handler(request):
	return render(template_name='index.html',context={},request=request)


def login_view_handler(request): 
	"""
	Handler for the login view; handles either GET or POST
	"""
	if request.method == "POST": # then they're trying to log in/submitting the form
		username,passwd = request.POST.get('username',''),request.POST.get('password','')
		if username != "" and passwd != "": 
			user = authenticate(request, username=username, password=passwd)
			if user is not None:
				login(request, user)
				return HttpResponseRedirect(request.POST.get('next','/'))
			else: 
				return render(request=request, template_name='login.html',context={'failed_login':1})
		else: 
			return render(request=request, template_name='login.html',context={'failed_login':1})
	elif request.method == "GET": # not submitting form
		return render(request=request,
				  template_name='login.html')


def logout_view_handler(request):
	""" Handler for the logout view """
	if request.user.is_authenticated: 
		logout(request)
	return HttpResponseRedirect("/")

def sign_up_view_handler(request): 
	""" handler for sign up view """

	if request.method == "POST": 
		# form submission; create account if valid
		rp = request.POST
		first_name,last_name,email,password = rp.get('first_name',None),rp.get('last_name',None),rp.get('username',None),rp.get('pwd1',None)
		background_color = rp.get('bgcolor',"#ffffff")
		bio = rp.get('bio',"Default Bio")
		if all([x is not None for x in [first_name,last_name,email,password]]):
			u = User.objects.create_user(first_name=first_name,last_name=last_name,email=email,username=email,password=password)
			u.save()
			p = Profile(user_id=u.id,bio=bio)
			p.save()
			login(request,u)
			return HttpResponseRedirect("/")
	elif request.method == "GET": # not submitting form
		return render(request=request,
				  template_name='sign_up.html')


def update_bio_handler(request): 
	"""
	Handler for updating bio (api call when bio is changed)
	"""
	bio = request.POST.get('bio',None)
	print("Bio: {}".format(bio))
	if bio is not None: 
		u = User.objects.get(id=request.user.id)
		u.profile.bio = bio.strip().replace("&nbsp;"," ")
		u.profile.save()
	return JsonResponse({})

def update_title_handler(request): 
	if request.method == "POST": 
		m = Meta.objects.all()[0]
		nt = request.POST.get('new_title','')
		m.navbar_title = nt
		m.site_title = nt
		m.save()
		return HttpResponse(json.dumps({'res':'succcess'}))

	else: 
		return HttpResponseRedirect("/")


def calendar_handler(request): 
	return render(template_name="calendar.html", context={},request=request)