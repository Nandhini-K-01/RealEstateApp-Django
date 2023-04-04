from django.shortcuts import render
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_protect, csrf_exempt, get_token
from .models import UserProfile
from django.contrib import messages

def home(request):
    return render(request, "property_list.html")

from .models import UserProfile

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        contact_number = request.POST['phone']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists! Please try a different username.")
            return redirect('home')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return redirect('home')
        
        if UserProfile.objects.filter(contact_number=contact_number).exists():
            messages.error(request, "Contact number already registered.")
            return redirect('home')
        
        if len(username)>20:
            messages.error(request, "Username must be under 20 characters.")
            return redirect('home')
        
        if pass1 != pass2:
            messages.error(request, "Passwords didn't match.")
            return redirect('home')
        
        if not username.isalnum():
            messages.error(request, "Username must be alpha-numeric.")
            return redirect('home')
            
        myuser = User.objects.create_user(username, email, pass1)
        profile = UserProfile(user=myuser, contact_number=contact_number)
        profile.save()

        messages.success(request, "Your account has been created successfully.")
        return redirect('signin')
        
    return render(request, "register.html")


def signin(request):
    next_url = request.POST.get('next') or request.GET.get('next') or reverse_lazy('property_list')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if next_url:
                return redirect(next_url)
            else:
                return redirect('property_list')
        else:
            messages.error(request, 'Invalid login credentials.')
            return render(request, 'login.html', {'next': next_url})
    else:
        return render(request, 'login.html', {'next': next_url})


# @csrf_protect
# def signin(request):
#     if request.method == 'POST':
#          # Validate CSRF token
#         csrf_token = request.POST.get('csrfmiddlewaretoken')
#         print(csrf_token)
#         if not csrf_token == request.session.get('csrf_token'):
#             messages.error(request, "Invalid CSRF token")
#             return redirect('home')
#         username = request.POST['username']
#         pass1 = request.POST['pass1']
        
#         user = authenticate(username=username, password=pass1)
        
#         if user is not None:
#             login(request, user)
#             fname = user.first_name
#             # messages.success(request, "Logged In Sucessfully!!")
            
#             return render(request, "authentication/index.html",{"fname":fname})
#         else:
#             messages.error(request, "Bad Credentials!!")
#             return redirect('home')
        
#     # Generate CSRF token and render login form
#     csrf_token = get_token(request)
#     request.session['csrf_token'] = csrf_token
#     return render(request, "authentication/signin.html", {'csrf_token': csrf_token})
#     # return render(request, "authentication/signin.html")


def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect('/')