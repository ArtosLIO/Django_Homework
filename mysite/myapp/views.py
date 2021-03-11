from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponse

from .form import MyForm, Login, CheckIn, ChangePass, GetComment
from .models import MyUser, Comment


def number(request, phone_number):
    return HttpResponse(f"<hr>\n<h1>User number: {phone_number}</h1>\n<hr>")

def some_str(request, string):
    return HttpResponse(f"<hr>\n<h1>You entered the correct string: {string}</h1>\n<hr>")

@login_required(login_url='/login')
def base(request):
    return render(request, 'first.html')

def index(request, article_number):
    return render(request, 'index.html', {'num': article_number})

def first(request, article_number, slug_text):
    return render(request, 'index.html',
                  {
                      'num': article_number,
                      'slug': slug_text,
                  })


@login_required(login_url='/login')
def check_form(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            accep = True
        else:
            accep = False
        return render(request, 'ready.html', {'accep': accep})
    else:
        form = MyForm()

    return render(request, 'first_valid.html', {'form': form})


def my_login(request):
    if request.method == 'POST':
        form = Login(request.POST)
        if form.is_valid():
            login(request, form.user)
            return render(request, 'first.html')
    else:
        form = Login()

    return render(request, 'login.html', {'form': form})


def my_logout(request):
    logout(request)
    form = Login()
    return render(request, 'login.html', {'form': form})


def check_in(request):
    if request.method == 'POST':
        form = CheckIn(request.POST)
        if form.is_valid():
            return render(request, 'first.html')
    else:
        form = CheckIn()

    return render(request, 'check_in.html', {'form': form})


@login_required(login_url='/login')
def change_pass(request):
    if request.method == 'POST':
        form = ChangePass(request.POST)

        if form.is_valid():
            username = request.user.username
            password = form.data['password']
            new_password = form.data['new_password']
            user = MyUser.objects.get(username=username)

            if user.check_password(raw_password=password):
                user.set_password(raw_password=new_password)
                user.save()
                return render(request, 'first.html')
            else:
                form.add_error(None, 'Password mismatch')
    else:
        form = ChangePass()

    return render(request, 'change_pass.html', {'form': form})


@login_required(login_url='/login')
def get_comment(request):
    comments = []
    if request.method == 'POST':
        form = GetComment(request.POST)
        if form.is_valid():
            text = form.data.get('text_comment', False)
            username = request.user.username
            if text:
                if 'comment_user' in form.data:
                    comments = Comment.objects.filter(Q(text__icontains=text) & Q(author__username=username)).values('text')
                else:
                    comments = Comment.objects.filter(text__icontains=text).values('text')
            else:
                if 'comment_user' in form.data:
                    comments = Comment.objects.filter(author__username=username).values('text')
                else:
                    comments = Comment.objects.all().values('text')
    else:
        form = GetComment()

    return render(request, 'get_comment.html', {'form': form, 'comments': comments})