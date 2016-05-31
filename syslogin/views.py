# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect
from django.contrib import auth
# from django.contrib.auth.models import User
from personal.models import MyUser as User
# from django.contrib.auth.forms import UserCreationForm
from personal.admin import UserCreationForm
from django.template.context_processors import csrf

# Create your views here.


def login(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(email=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            args['login_error'] = 'Пользователь не найден'
            return render_to_response('login.html', args)
    else:
        return render_to_response('login.html', args)


def logout(request):
    logout(request)
    return redirect('/')


def register(request):
    args = {}
    args.update(csrf(request))
    args['form'] = UserCreationForm()
    if request.POST:
        newuser_form = UserCreationForm(request.POST)
        if newuser_form.is_valid():
            newuser_form.save()
            newuser = auth.authenticate(email=newuser_form.cleaned_data['email'], password=newuser_form.cleaned_data['password1'])
            auth.login(request, newuser)
            return redirect('/')
        else:
            args['form'] = newuser_form
    return render_to_response('register.html', args)

