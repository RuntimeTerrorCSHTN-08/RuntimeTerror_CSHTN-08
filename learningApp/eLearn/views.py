from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from django.contrib.auth import authenticate , login, logout
from django.contrib.auth.models import User
from django.core.mail import send_mail

# Create your views here.
def index(request):
  # messages.success(request, "This is a test Message!!")
  return render(request,"landing.html")

def course_frontend(request):
  return render(request,"course_frontend.html")
def course_backend(request):
  return render(request,"course_backend.html")
def course_database(request):
  return render(request,"course_database.html")

def handleSignup(request):
  if request.method == "POST":
    #GET THE POST PARAMETERS
    username = request.POST['username']
    fname = request.POST['fname']
    email = request.POST['email']
    pass1 = request.POST['pass1']
    pass2 = request.POST['pass2']

    # Check for errorneous inputs
    if len(username) >10:
      messages.warning(request, "Username must be under 10 characters")
      return redirect('home')

    if not username.isalnum():
      messages.warning(request, "Username should only contain letters and numbers")
      return redirect('home')

    if (pass1 != pass2):
      messages.warning(request, "Password do not match")
      return redirect('home')

    # Create the user
    myuser = User.objects.create_user(username, email, pass1)
    myuser.first_name = fname
    myuser.save()
    messages.success(request, "Your StackUp account has been successfully created!!")
    return redirect('home')
  else:
    return HttpResponse('404 - NOT FOUND')

def handleLogin(request):
  if request.method == "POST":
    #GET THE POST PARAMETERS
    loginusername = request.POST['loginusername']
    loginpassword = request.POST['loginpassword']
    user =  authenticate(username = loginusername, password = loginpassword)
    if user is not None:
      login(request, user)
      messages.success(request, "Successfully Logged In!!")
      return redirect('home')
    else:
      messages.warning(request, "Invalid Credentials, Please try again")
      return redirect('home')
  else:
    return HttpResponse('404 - NOT FOUND')

def handleLogout(request):
  logout(request)
  messages.success(request, "Successfully Logged Out!!")
  return redirect('home')


def handleContact(request):
  if request.method == 'POST':
    # send mail
    message_email = request.POST['sendEmail']

    # To send an email
    send_mail(
      'From - StackUp', #subject
       message_email, #message
       message_email, #from email
       ['nidnac2@gmail.com'], #to email
    )
    
    if message_email:
      messages.success(request, "We recieved your email and will respond shortly...")
    else: 
      messages.warning(request, "Please enter an email-address")
    return render(request, 'landing.html', {'message_email' : message_email})
  else:
    return render(request, 'landing.html', {})


