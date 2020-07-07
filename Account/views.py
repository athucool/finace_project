from django.shortcuts import render
from django.http import HttpResponse
from .forms import SignUpForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def Register(request):

    registered=False

    if request.method == 'POST':


        user_form=SignUpForm(data=request.POST)
 
        if user_form.is_valid():
            user_form.save() 
            username = request.POST.get('username')
            print("request.user.pk",request.user.pk)
            user=User.objects.get(username=username)
            print("user",user)
            user.save()
            

            registered=True
        
        else:
            return HttpResponse(user_form.errors)
    else:
        user_form=SignUpForm()
         
    return render(request,'Account/register.html',{'user_form':user_form,'registered':registered})



def user_login(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)

                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse("account not active")
        else:
            return HttpResponse("check your username and password")
            print("failed to login") 
            print("username{} password{}".format(username,password))
    else:
        return render(request,'Account/login.html',{})



@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))



def index(request):
    return render(request,'Account/index.html')
