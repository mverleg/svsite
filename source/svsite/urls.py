"""
svsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
	https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
	1. Add an import:  from my_app import views
	2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
	1. Add an import:  from other_app.views import Home
	2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
	1. Add an import:  from blog import urls as blog_urls
	2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""

from django.conf.urls import include, url
from django.contrib import admin
from django.http import HttpResponse
import grappelli.urls
import allauth.urls
import member.urls
import activity.urls
try:
	from svsite.playground import playground
except ImportError:
	playground = lambda request: HttpResponse('nothing here')


urlpatterns = [
	url(r'^$', lambda request: HttpResponse('under construction')),
	url(r'^test/$', playground),
	url(r'^grappelli/', include(grappelli.urls)),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^account/', include(allauth.urls)),
	url(r'^member/', include(member.urls)),
	url(r'^activity/', include(activity.urls)),
]


