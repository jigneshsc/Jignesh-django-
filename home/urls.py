from django.contrib import admin
from django.urls import path
from home import views

admin.site.site_header = "Jignesh Singh Chauhan"
admin.site.site_title = "Jignesh Admin Portal"
admin.site.index_title = "Welcome to Jignesh Singh Chauhan Researcher Portal"

urlpatterns = [
    path('', views.index, name='home')




]