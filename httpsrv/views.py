from httpsrv.viewhandlers import *
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.contrib.auth.decorators import login_required

def index(request): 
    """ Home page view"""
    return index_handler(request)

def login_view(request):
    """ View for logging in """
    if request.user.is_authenticated:
        return HttpResponseRedirect("/")
    else:
        return login_view_handler(request)

def logout_view(request):
    return logout_view_handler(request)


def sign_up_view(request):
    return sign_up_view_handler(request)

@login_required
def calendar(request): 
    return calendar_handler(request)

# Meta Updates 

@csrf_exempt
def update_background(request):
    return update_background_handler(request)

@csrf_exempt
@login_required
def update_bio(request):
    return update_bio_handler(request)

@login_required
def update_title(request): 
    return update_title_handler(request)

@login_required
def review(request): 
    return review_handler(request)