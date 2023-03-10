from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q


# Create your views here.
@login_required(login_url='login')
def Homepage(request):
     notes=Notes.objects.filter(user_id=request.user.id)
     
     context={
         'notes':notes
     }


     return render(request,'home.html',context)


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
            return redirect('login')
         

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

    
@login_required(login_url='login')
def addnotes(request):
      form=AddNotesForm()

      if request.method=="POST":
          form=AddNotesForm(request.POST)
          if form.is_valid():
              var=form.save(commit=False)
              var.user=request.user
              var.save()
              messages.success(request,'added succesfully')
              return redirect('/')

      context={
          "form":form
      }
      


      return render(request,'addnote.html',context)


def deletepage(request,pk):
    Note=Notes.objects.get(id=pk)
    context={
        'Note':Note
    }
   
    if request.method=="POST":
        Note.delete()
        messages.success(request,'succesfully deleted')
        return redirect('/')

    

    return render(request,'delete.html',context)

    


def updatepage(request,pk):
    Note=Notes.objects.get(id=pk)
    
    form=AddNotesForm(instance=Note)

    if request.method=="POST":
        form=AddNotesForm(request.POST,instance=Note)
        if form.is_valid():
            form.save()
            messages.success(request,'succesfully updated')
            
            return redirect('/')
    context={
        'Note':Note,
        'form':form
    }

    return render(request,'updatenote.html',context)
   

def viewnote(request,pk):
    note=Notes.objects.get(id=pk)

    context={
        "note":note
    }

    return render(request,'viewnote.html',context)
    

def searchfunction(request):
    query=request.GET.get('query')

    notes=Notes.objects.filter(Q(title__icontains=query)|Q(description__icontains=query))

    context={
        'query':query,
        'notes':notes
    }

    return render(request,'search.html',context)
