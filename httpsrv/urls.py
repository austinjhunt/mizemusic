app_name = "httpsrv"
from django.conf.urls import url
from django.urls import path
from . import views
from django.http import HttpResponseRedirect
urlpatterns = [
    url(r'^$', views.index),
    
    # Account mgmt
    url(r'^login',views.login_view),
    url(r'^logout',views.logout_view),
    url(r'^sign_up',views.sign_up_view),
    # profile 
    url(r'^update_bio',views.update_bio),

    # Calendar
    url(r'^calendar',views.calendar), 
    

    # meta updates
    url(r'^update_title',views.update_title),

    url(r'^review',views.review), 

]