from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def index(request):
	return render(request,'html/index.html')

def admin_login(request):
	return render(request,'html/admin_login.html')

def user_login(request):
    error=""
    if request.method == "POST":
        u = request.post['uname'];
        p = request.post['pwd'];
        user = authenticate(username=u,password=p)
        if user:
            try:
                user1 = StudentUser.objects.get(user=user)
                if user1.type == "student":
                    login(request,user)
                    error="no"
                else:
                    error="yes"
            except:
                error="yes"
        else:
            error="yes"
    d = {'error:error'}
    return render(request,'html/user_login.html',d)

def recruiter_login(request):
	return render(request,'html/recruiter_login.html')

def recruiter_signup(request):
	return render(request,'html/recruiter_signup.html')


def user_home(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    return render(request,'html/user_home.html')

def Logout(request):
    logout(request)
    return redirect('index')

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



def admin_home(request):
	if not request.user.is_authenticated:
		return redirect('admin_login')
	return render(request,'html/admin_home.html')





def view_users(request):
	if not request.user.is_authenticated:
		return redirect('admin_login')
	data = StudentUser.objects.all()
	d:{'data':data}
	return render(request,'html/view_users.html',d)



#video:27
def delete_user(request,pid):
	if not request.user.is_authenticated:
		return redirect('admin_login')
	data = StudentUser.objects.get(id=pid)
	student.delete()
	return redirect('/view_users')

def recruiter_pending(request):
	if not request.user.is_authenticated:
		return redirect('admin_login')
	data = Recruiter.objects.filter(status='pending')
	d:{'data':data}
	return render(request,'html/recruiter_pending.html',d)


def change_status(request,pid):
	if not request.user.is_authenticated:
		return redirect('admin_login')
	error=""
	recruiter = Recruiter.objects.get(id = pid )
	if request.method == "POST":
		s = request.POST['status']
		recruiter.status = s
		try:
			recruiter.save()
			error = "no"
		except:
			error= "yes"
	d:{'recruiter':recruiter,'error':error}
	return render(request,'html/change_status.html',d)

	