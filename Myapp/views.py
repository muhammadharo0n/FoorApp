from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserForm
from .models import *
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request ,"home.html")

def registerUser(request):
    if request.method == 'POST':
        print(request.POST)
        form = UserForm(request.POST)

        if form.is_valid():
            password = form.cleaned_data['password']
            user = form.save(commit=False)
            user.set_password (password)
            user.role = User.COSTUMER
            user.save()
            messages.success(request , "Your account has been registedred successfully")

            return redirect('registerUser')
        
        else:
            print('Form Invalid') 
            print(form.errors)

    else: 
        form = UserForm()
    context = {
        'form':form,
    }
    return render(request , 'MyAppOne/registerUser.html',context)