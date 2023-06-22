from http.client import HTTPResponse
from django.shortcuts import render, redirect
from users.models import User
from django.contrib.auth import login,authenticate

# Create your views here.
def register(request):
   if request.method == "POST":
       username = request.POST.get('username')
       email = request.POST.get('email')
       password1 = request.POST.get('password1')
       password2 = request.POST.get('password2')
       phone = request.POST.get('phone')
       if password1 == password2:
           user = User.objects.create(username = username,email=email,phone=phone)
           user.set_password(password1)
           user.save()
           user = User.objects.get(username=username)
           user.authenticate(username, password=password1)
           login(request, user)
           return redirect('index')
       else:
           return HTTPResponse('Пароли не совпадают')
           
           
   return render(request, 'register.html')


def user_login(request):
    if request.method == "POST":
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = User.objects.get(username = username)
            user = authenticate(username = username, password = password)
            login(request, user)
            return redirect('index')
        except:
            return HTTPResponse("Неправильные данные")
    return render(request, 'login.html')