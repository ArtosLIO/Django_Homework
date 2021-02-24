from django.urls import path, re_path
from .views import *


urlpatterns = [
    path('<int:some_num>', first),
    path('article/<int:article_numer>/', article),
    path('article/<int:article_numer>/archive/', article_archive),
    path('article/<int:article_numer>/<slug:slug_text>', article),
    path('acricles/', acricles),
    path('acricles/archive/', archive),
    path('users/', users),
    re_path(r'^number/(050\d{7}|0[679]{1}3\d{7}|06[6-8]{1}\d{7}|09[5-9]{1}\d{7})/$', number),
    re_path(r'^string/([0-9a-f]{4}\-[0-9a-f]{6})/$', some_str),
]