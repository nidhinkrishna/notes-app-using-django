from django.shortcuts import render,redirect
from .forms import *


# Create your views here.
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
            return redirect('/')

    return render(request,'signup.html',context)