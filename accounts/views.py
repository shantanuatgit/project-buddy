from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth


def signup(request, backend='django.contrib.auth.backends.ModelBackend'):
    if request.method=="POST":   # if user submit the info.  then if block will execute
        # user wants to create account
        if request.POST['password1']==request.POST['password2']:
            # check if user already exists
            try:
                user=User.objects.get(username=request.POST['Username'])
                return render(request,'accounts/signup.html',{'error':'username already taken'})
            except User.DoesNotExist:
                user=User.objects.create_user(request.POST['Username'],password=request.POST['password1'])
                auth.login(request,user, backend='django.contrib.auth.backends.ModelBackend')  #this line automatically log that user in
                return redirect('filldetails')
        else:
            return render(request,'accounts/signup.html',{'error':'password must match'})
    else:
        # this will first show signup page to create account
        return render(request,'accounts/signup.html')


def login(request, backend='django.contrib.auth.backends.ModelBackend'):
    if request.method=="POST":
        user=auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            return render(request,'accounts/signup.html',{'error':'username or password is incorrect'})
    else:
        return render(request,'accounts/signup.html')


def logout(request, backend='django.contrib.auth.backends.ModelBackend'):
    if request.method=="POST":
        auth.logout(request)
        return redirect('/')
