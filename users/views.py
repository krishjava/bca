from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth

def register(request):
    if request.method == 'POST':
        user=request.POST['username']
        user=user.strip()
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        email_qs = User.objects.filter(email=email)
        if not email_qs.exists():
            if password1==password2:
                try:
                    User.objects.get(username=user)
                    return render(request,"register.html",{'user_msg':'User name Already Taken'})
                except User.DoesNotExist:
                    user=User.objects.create_user(username=user,password=password1,email=email)
                    auth.login(request,user)
                    return  redirect('/')
            else:
                return render(request,"register.html",{'pass_msg':'Password not Matched'})
        else:
            return render(request,"register.html",{'email_msg':'Email Already Taken'})
    return render(request,"register.html")
