from django.contrib.auth import authenticate
from django import forms
from django.core.exceptions import ValidationError

from .models import MyUser

GENDER = [
    ('N', 'None'),
    ('M', 'Man'),
    ('W', 'Woman'),
]
SKILL_ENGLISH = [
    (0, 'A1 - Elementary'),
    (1, 'A2 - Pre Intermediate'),
    (2, 'B1 - Intermediate'),
    (3, 'B2 - Upper Intermediate'),
    (4, 'C1 - Advanced'),
    (5, 'C2 - Proficient'),
]


class MyForm(forms.Form):
    name = forms.CharField(label='Your nickname', max_length=150)
    gender = forms.ChoiceField(label='Your gender', choices=GENDER)
    age = forms.IntegerField(label='Your age', min_value=16, max_value=100)
    skill = forms.ChoiceField(label='Your skill english language', choices=SKILL_ENGLISH)

    def clean(self):
        cleaned_data = super().clean()
        gender = cleaned_data.get('gender')
        age = cleaned_data.get('age')
        skill = int(cleaned_data.get('skill'))
        if gender == 'M' and age > 20 and skill > 2:
            pass
        elif gender == 'W' and age > 22 and skill > 1:
            pass
        else:
            self.add_error(None, 'This form always incorrect')


class Login(forms.Form):
    username = forms.CharField(label='Your user name', max_length=150)
    password = forms.CharField(label='Your password', widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        if username and password:
            self.user = authenticate(username=username, password=password)
            if self.user is None:
                self.add_error(None, 'Username or password incorrect')


class CheckIn(forms.Form):
    username = forms.CharField(label='Your user name', max_length=150)
    password = forms.CharField(label='Your password', widget=forms.PasswordInput())
    check_pass = forms.CharField(label='Confirm your password', widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        check_pass = cleaned_data.get('check_pass')

        if password != check_pass:
            return self.add_error(None, 'Password do not equally')
        if len(MyUser.objects.filter(username=username)):
            return self.add_error(None, 'Username is taken')

        MyUser.objects.create_user(username=username, password=password)


class ChangePass(forms.Form):
    password = forms.CharField(label='Your password', widget=forms.PasswordInput())
    new_password = forms.CharField(label='Your new password', widget=forms.PasswordInput())
    check_pass = forms.CharField(label='Confirm your password', widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        new_password = cleaned_data.get('new_password')
        check_pass = cleaned_data.get('check_pass')

        if password == new_password:
            self.add_error(None, 'This password is used')
        if new_password != check_pass:
            self.add_error(None, 'Password mismatch')


class GetComment(forms.Form):
    text_comment = forms.CharField(label='Enter text comment', max_length=150, required=False)
    comment_user = forms.BooleanField(label='Comment user', required=False, initial=False)

    def clean(self):
        super().clean()