from django.shortcuts import render,redirect
from django.contrib import messages,auth

# user model for checking duplicate email
from django.contrib.auth.models import User

# Create your views here.
def register(request):
  if request.method=='POST':
    # messages.error(request, 'Testing error message')
    # return redirect('register')

    # Get form values
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    password2  = request.POST['password2']

    # Check password match
    if password == password2:
      # Check username
      if User.objects.filter(username=username).exists(): #(database_username=variable_username)
        messages.error(request,'Username already taken')
        return redirect('register')
      else:
        if User.objects.filter(email=email).exists():
          messages.error(request,'The email is being used')
          return redirect('register')
        else:
          # Looks good Register the user
          user=User.objects.create_user(username = username, email = email, password = password,first_name = first_name,last_name = last_name)
          
          # Login automatically after register
          # auth.login(request,user) #we need to import auth
          # messages.success(request,'You are now logged in')
          # return redirect('/')

          user.save()
          messages.success(request, 'you are successfully registered and can log in')
          return redirect('login')
    else:
      messages.error(request, 'Passwords donot match')
      return redirect('register')
  else:
    return render(request,'accounts/register.html')

def login(request):
  if request.method=='POST':
    # Get the values from input
    username=request.POST['username']
    password=request.POST['password']
    
    # login/authenticate
    user=auth.authenticate(username = username, password = password)

    if user is not None:
      auth.login(request,user)
      messages.success(request,'You are now logged in')
      return redirect('dashboard')
    else:
      messages.error(request,'Invalid credentials')
      return redirect('login')
  else:
    return render(request,'accounts/login.html')

def logout(request):
  if request.method=='POST':
    auth.logout(request)
    messages.success(request,'You are successfully logged out')
    return redirect('index')

def dashboard(request):
  return render(request,'accounts/dashboard.html')
