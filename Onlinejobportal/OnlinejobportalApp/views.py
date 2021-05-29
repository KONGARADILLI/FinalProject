from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

# Create your views here.
def index(request):
	return render(request,'html/index.html')

def admin_login(request):
	return render(request,'html/admin_login.html')

def user_login(request):
	error=""
	if request.method == "POST":
		u = request.POST['uname'];
		p = request.POST['pwd'];
		user = authenticate(username=u,password=p)
		if user:
			try:
				user1 = StudentUser.objects.get(user=user)
				if user1.type == "student":
					login(request,user)
					error="no"
				else:
					error = "yes"
			except:
				error="yes"
	else:
		error="Yes"
		d={'error':error}
	return render(request,'html/user_login.html')

def recruiter_login(request):
	return render(request,'html/recruiter_login.html')


def user_home(request):
	if not request.user.is_authenticated:
		return redirect('/user_login')
	return render(request,'html/user_home.html')

def user_signup(request):
	error=""
	if request.method == 'POST':
		f = request.POST['fname']
		l = request.POST['lname']
		i = request.FILES['image']
		p = request.POST['pwd']
		e = request.POST['email']
		con = request.POST['contact']
		gen = request.POST['gender']
		try:
			user = User.objects.create_user(first_name=f,last_name=l,username=e,password=p)
			StudentUser.objects.create(user=user,mobile=con,image=i,gender=gen,type="student")
			error="no"
		except:
			error="yes"
			d={'error':error}
	return render(request,'html/user_signup.html')