from django.urls import re_path
from . import views
react_views_regex = r'\/|\b'.join(['','/','/login',]) + r'\/'

urlpatterns = [
    re_path(r'.*', views.home)
]