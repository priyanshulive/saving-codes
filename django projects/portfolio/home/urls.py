from django.contrib import admin
from django.urls import path,include
from home import views

# Django admin header customization
admin.site.site_header="Web Developer"
admin.site.site_title="Dashboard"
admin.site.index_title="Welcome"


urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('project', views.project, name='project'),
    path('contact', views.contact, name='contact')
]