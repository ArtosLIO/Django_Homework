from django.shortcuts import render
from django.http import HttpResponse


def first(request, some_num):
    return HttpResponse(f"Hey! It's {some_num*2}")

def article(request, article_numer, slug_text=''):
    return HttpResponse(
        "This is an article #{}. {}".format(article_numer, "Name of this article is {}".format(
            slug_text) if slug_text else "This is unnamed article"))

def article_archive(request, article_numer):
    return HttpResponse(f"<h1>Article Archive</h1>\n<h2>{article_numer}</h2>")

def acricles(request):
    return HttpResponse("<h1>Acricles</h1>")

def archive(request):
    return HttpResponse("<h1>Acricles</h1>\n<h2>Archive</h2>")

def users(request):
    return HttpResponse("<hr>\n<h1>Users</h1>\n<hr>")

def number(request, phone_number):
    return HttpResponse(f"<hr>\n<h1>User number: {phone_number}</h1>\n<hr>")

def some_str(request, string):
    return HttpResponse(f"<hr>\n<h1>You entered the correct string: {string}</h1>\n<hr>")

