"""project7 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import re_path as url
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from fstapp.views import index
from cloud import views as cloud
from admn import views as admn
from user import views as user
from project7 import views as cloudmonitor

urlpatterns = [
    url(r'^admn/', admin.site.urls),
    url(r'^index/', index, name="index"),

    path(r'userlogin', user.userlogin, name='userlogin'),
    path(r'userregister', user.userregister, name='userregister'),
    path(r'storeregistration', user.storeregistration, name='storeregistration'),
    path(r'userlogincheck', user.userlogincheck, name='userlogincheck'),
    path(r'usercreateapp',user.usercreateapp,name='usercreateapp'),
    path(r'appcreaterequest',user.appcreaterequest,name='appcreaterequest'),
    path(r'useruploadfile/<appname>/$',user.useruploadfile,name='useruploadfile'),
    path(r'^snippet_detail/$',user.snippet_detail,name='snippet_detail'),
    path(r'clddeletefile',user.clddeletefile,name='clddeletefile'),
    path(r'cldresturl',user.cldresturl,name='cldresturl'),
    path(r'accounts', user.AccountAPIView.as_view(), name='account-list'),
    path(r'contacts', user.ContactAPIView.as_view(), name='contact-list'),
    path(r'activities', user.ActivityAPIView.as_view(), name='activity-list'),
    path(r'activitystatuses', user.ActivityStatusAPIView.as_view(), name='activity-status-list'),
    path(r'contactsources', user.ContactSourceAPIView.as_view(), name='contact-source-list'),
    path(r'contactstatuses', user.ContactStatusAPIView.as_view(), name='contact-status-list'),
    path(r'logout',user.logout,name='logout'),




    url(r'^adminlogin/',admn.adminlogin, name="adminlogin"),
    path(r'adminlogincheck',admn.adminlogincheck,name='adminlogincheck'),
    path(r'adminactivateusers',admn.adminactivateusers,name='adminactivateusers'),
    path(r'activatewaitedusers/<id>/$',admn.activatewaitedusers,name='activatewaitedusers'),


    path(r'cloudlogin',cloud.cloudlogin,name='cloudlogin'),
    path(r'cloudlogincheck',cloud.cloudlogincheck,name='cloudlogincheck'),
    path(r'activateuserapp',cloud. activateuserapp, name='activateuserapp'),
    path(r'cloudlogincheck',cloud. cloudlogincheck, name='cloudlogincheck'),
    path(r'clouduserappactivations/<appname>/$',cloud. clouduserappactivations, name='clouduserappactivations'),


    path(r'uploadfile',cloudmonitor.uploadfile,name='uploadfile'),
    path(r'deletefile/<id>',cloudmonitor.deletefile,name='deletefile'),
    path(r'downloadfile/<id>',cloudmonitor.downloadfile,name='downloadfile'),
    path(r'resturl/<id>',cloudmonitor.resturl,name='resturl'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)