from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.
@login_required(login_url='login')
def Homepage(request):


     return render(request,'home.html')


def signup(request):
    form=RegistrationForm()
    context={
        'form':form
     }

    if request.method == "POST":
        form=RegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request,'registration success you can login now')
            return redirect('/')
         

    return render(request,'signup.html',context)
  




def loginPage(request):

    if request.method =="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            messages.success(request,'login success')
            return redirect('/')
        else:
            messages.error(request,'invalid username')
        

    return render(request,'login.html')


def logoutfunction(request):

    if request.user.is_authenticated:
        logout(request)
        messages.success(request,'succesfully loged out ')
        return redirect('login')

    
