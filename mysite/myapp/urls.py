from django.urls import path, re_path
from .views import *


urlpatterns = [
    path('', check_form, name='form'),

    path('logout', my_logout, name='logout'),
    path('login/', my_login, name='login'),
    path('registration/', check_in, name='check_in'),
    path('changepass/', change_pass, name='change_pass'),

    path('getcomment/', get_comment, name='get_comment'),

    path('base/', base, name='base'),
    path('article/<int:article_number>/', index, name='index'),
    path('article/<int:article_number>/<slug:slug_text>/', first, name='first'),

    re_path(r'^number/(050\d{7}|0[679]{1}3\d{7}|06[6-8]{1}\d{7}|09[5-9]{1}\d{7})/$', number),
    re_path(r'^string/([0-9a-f]{4}\-[0-9a-f]{6})/$', some_str),
]