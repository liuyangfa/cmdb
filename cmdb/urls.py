from django.conf.urls import url
from django.contrib import admin

from base import views

urlpatterns = [
    url(r'^$', views.redirect),
    url(r'^login/', views.login),
    url(r'^index/', views.index),
    url(r'^member_del/', views.member_del),
    url(r'^member_add/', views.member_add),
    url(r'^member_list/$', views.member_list),
    url(r'^member_search/', views.member_search),
    url(r'^member_edit/([0-9]{0,4})/', views.member_edit),
    url(r'^admin/', admin.site.urls),
]
