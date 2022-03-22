import re
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from .forms import UserForm
from django.contrib.auth.decorators import login_required
# from django.utils.decorators import method_decorator--

# from .forms import *

def register(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            password = request.POST['password']
            user_type = request.POST['user_type']
            user=User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email)
            user.set_password(password)
            if user_type == "Product":
                product_admin=Group.objects.get(id=2)
                product_admin.user_set.add(user)
            else:
                customer=Group.objects.get(id=1)
                customer.user_set.add(user)

            user.save()
            return render (request=request, template_name="login.html")
    form = UserForm()
    return render (request=request, template_name="register.html", context={"form":form})


def login(request):
    # if request.user.is_authenticated:
    #     return redirect('customer')
    # else:
    if request.method == 'POST':
        username = request.POST.get('username')
        password =request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            print(user)
            if user.groups.filter(id=1).exists():
                # print("#######################")
                print(request.user)
            # login(request, user)
                return redirect('customer')
            else:
                print("............................")
                return redirect('product_admin1')
        else:
            return render(request, 'login.html')    
    else:
    # context = {}
        return render(request, 'login.html')



# @login_required(redirect_field_name=)
def customer(request):

    return render(request, 'customer.html')
    # return render(request, 'product_admin.html')

# @login_required
def product_admin(request):
    return render(request, 'product_admin.html')

def logout(request):
    # logout(request)
    return redirect('login')

def trail(request):
    return render(request, 'footer.html')



    #####################################################################
