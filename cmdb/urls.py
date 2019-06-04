"""cmdb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from base.views import *

urlpatterns = [
    url(r'^$', login),
    url(r'^member_search/', member_search),
    url(r'^login/', login),
    url(r'^index/', index),
    url(r'^member_add/', member_add),
    url(r'^member_del/', member_del),
    url(r'^member_edit/([0-9]{0,4})/', member_edit),
    url(r'^member_list/', member_list),
    url(r'^admin/', admin.site.urls),
]
