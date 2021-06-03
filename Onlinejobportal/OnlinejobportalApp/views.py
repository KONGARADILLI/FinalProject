from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from datetime import date

# Create your views here.
def index(request):
	return render(request,'html/index.html')

def admin_login(request):
	error=""
	if request.method == "POST":
		u = request.POST['uname']
		p = request.POST['pwd']
		user = authenticate(username=u,password=p)
		try:
			if user.is_staff:
				login(request,user)
				error="no"
			else:
				error="yes"
		except:
			error = "yes"
	d={'error':error}
	return render(request,'html/admin_login.html',d)

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
                    error="yes"
            except:
                error="yes"
        else:
            error="yes"
    d = {'error':error}
    return render(request,'html/user_login.html',d)


def recruiter_login(request):
    error=""
    if request.method == "POST":
        u = request.POST['uname'];
        p = request.POST['pwd'];
        user = authenticate(username=u,password=p)
        if user:
            try:
                user1 = Recruiter.objects.get(user=user)
                if user1.type == "recruiter" and user1.status != "pending":
                    login(request,user)
                    error="no"
                else:
                    error="not"
            except:
                error="yes"
        else:
            error="yes"
    d = {'error':error}
    return render(request,'html/recruiter_login.html',d)


def recruiter_signup(request):
	error=""
	if request.method == 'POST':
		f = request.POST['fname']
		l = request.POST['lname']
		i = request.FILES['image']
		p = request.POST['pwd']
		e = request.POST['email']
		con = request.POST['contact']
		gen = request.POST['gender']
		com = request.POST['company']
		try:
			user = User.objects.create_user(first_name=f,last_name=l,username=e,password=p)
			Recruiter.objects.create(user=user,mobile=con,image=i,gender=gen,type="recruiter",company=com ,status="pending")
			error="no"
		except:
			error="yes"
	d={'error':error}
	return render(request,'html/recruiter_signup.html',d)


def user_home(request):
    if not request.user.is_authenticated:
        return redirect('user_login/')
    return render(request,'html/user_home.html')

def recruiter_home(request):
    if not request.user.is_authenticated:
        return redirect('recruiter_login')
    user = request.user
    recruiter = Recruiter.objects.get(user=user)
    error=""
    if request.method == 'POST':
    	f = request.POST['fname']
    	l = request.POST['lname']
    	con = request.POST['contact']
    	gen = request.POST['gender']
    	recruiter.user.first_name = f
    	recruiter.user.last_name = l
    	recruiter.user.mobile = con
    	recruiter.user.gender = gen
    	try:
    		recruiter.save()
    		recruiter.user.save()
    		error="no"
    	except:
    		error="yes"
    	try:
    		i = request.FILES['image']
    		recruiter.image = i
    		recruiter.save()
    		error="no"
    	except:
    		pass
    d={'recruiter':recruiter,'error':error}
    return render(request,'html/recruiter_home.html',d)


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
	return render(request,'html/user_signup.html',d)



def admin_home(request):
	if not request.user.is_authenticated:
		return redirect('admin_login')
	return render(request,'html/admin_home.html')





def view_users(request):
	if not request.user.is_authenticated:
		return redirect('admin_login')
	data = StudentUser.objects.all()
	d={'data':data}
	return render(request,'html/view_users.html',d)



def delete_user(request,pid):
	if not request.user.is_authenticated:
		return redirect('admin_login')
	student = User.objects.get(id=pid)
	student.delete()
	return redirect('/view_users')

def delete_recruiter(request,pid):
	if not request.user.is_authenticated:
		return redirect('admin_login')
	recruiter = User.objects.get(id=pid)
	recruiter.delete()
	return redirect('/recruiter_all')

def delete_job(request,pid):
	if not request.user.is_authenticated:
		return redirect('recruiter_login')
	job = Job.objects.get(id=pid)
	job.delete()
	return redirect('/job_list')

def recruiter_pending(request):
	if not request.user.is_authenticated:
		return redirect('admin_login')
	data = Recruiter.objects.filter(status='pending')
	d={'data':data}
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
	d={'recruiter':recruiter,'error':error}
	return render(request,'html/change_status.html',d)

def recruiter_accepted(request):
	if not request.user.is_authenticated:
		return redirect('admin_login')
	data = Recruiter.objects.filter(status='Accept')
	d={'data':data}
	return render(request,'html/recruiter_accepted.html',d)

def recruiter_rejected(request):
	if not request.user.is_authenticated:
		return redirect('admin_login')
	data = Recruiter.objects.filter(status='Reject')
	d={'data':data}
	return render(request,'html/recruiter_rejected.html',d)

def recruiter_all(request):
	if not request.user.is_authenticated:
		return redirect('admin_login')
	data = Recruiter.objects.all()
	d={'data':data}
	return render(request,'html/recruiter_all.html',d)

def change_passwordadmin(request):
	if not request.user.is_authenticated:
		return redirect('admin_login')
	error=""
	if request.method == "POST":
		c = request.POST['currentpassword']
		n = request.POST['newpassword']
		try:
			u = User.objects.get(id=request.user.id)
			if u.check_password(c):
				u.set_password(n)
				u.save()
				error = "no"
			else:
				error = "yes"
		except:
			error= "yes"
	d={'error':error}
	return render(request,'html/change_passwordadmin.html',d)

def change_passworduser(request):
	if not request.user.is_authenticated:
		return redirect('user_login')
	error=""
	if request.method == "POST":
		c = request.POST['currentpassword']
		n = request.POST['newpassword']
		try:
			u = User.objects.get(id=request.user.id)
			if u.check_password(c):
				u.set_password(n)
				u.save()
				error = "no"
			else:
				error = "yes"
		except:
			error= "yes"
	d={'error':error}
	return render(request,'html/change_passworduser.html',d)


def change_passwordrecruiter(request):
	if not request.user.is_authenticated:
		return redirect('recruiter_login')
	error=""
	if request.method == "POST":
		c = request.POST['currentpassword']
		n = request.POST['newpassword']
		try:
			u = User.objects.get(id=request.user.id)
			if u.check_password(c):
				u.set_password(n)
				u.save()
				error = "no"
			else:
				error = "yes"
		except:
			error= "yes"
	d={'error':error}
	return render(request,'html/change_passwordrecruiter.html',d)

def add_job(request):
	if not request.user.is_authenticated:
		return redirect('recruiter_login')
	error=""
	if request.method == 'POST':
		jt = request.POST['jobtitle']
		sd = request.POST['startdate']
		ed = request.POST['enddate']
		sal = request.POST['salary']
		l = request.FILES['logo']
		exp = request.POST['experience']
		loc = request.POST['location']
		skills = request.POST['skills']
		des = request.POST['description']
		com = request.POST['company']
		user = request.user

		recruiter = Recruiter.objects.get(user=user)
		try:
			Job.objects.create(recruiter=recruiter,start_date = sd,end_date=ed,title=jt,salary=sal,image=l,
			description= des,experience = exp,location=loc,skills=skills,creationdate =date.today(),company=com)
			error="no"
		except:
			error="yes"
		print(com)
	d={'error':error}
	return render(request,'html/add_job.html',d)

def job_list(request):
    if not request.user.is_authenticated:
    	return redirect('recruiter_login')
    user = request.user
    recruiter = Recruiter.objects.get(user=user)
    job = Job.objects.filter(recruiter = recruiter)
    d={'job':job}
    return render(request,'html/job_list.html',d)

def edit_jobdetail(request,pid):
	if not request.user.is_authenticated:
		return redirect('recruiter_login')
	error=""
	job = Job.objects.get(id=pid)
	if request.method == 'POST':
		jt = request.POST['jobtitle']
		sd = request.POST['startdate']
		ed = request.POST['enddate']
		sal = request.POST['salary']
		exp = request.POST['experience']
		loc = request.POST['location']
		skills = request.POST['skills']
		des = request.POST['description']

		job.title = jt
		job.salary = sal
		job.experience = exp
		job.location = loc
		job.skills = skills
		job.description = des
		try:
			job.save()
			error="no"
		except:
			error="yes"
		if sd:
			try:
				job.start_date = sd
				job.save()
			except:
				pass
		else:
			pass
		if ed:
			try:
				job.end_date = ed
				job.save()
			except:
				pass
		else:
			pass
	d={'error':error,'job':job}
	return render(request,'html/edit_jobdetail.html',d)



def change_companylogo(request,pid):
	if not request.user.is_authenticated:
		return redirect('recruiter_login')
	error=""
	job = Job.objects.get(id=pid)
	if request.method == 'POST':
		cl = request.FILES['logo']
		job.image = cl
		try:
			job.save()
			error="no"
		except:
			error="yes"
	d={'error':error,'job':job}
	return render(request,'html/change_companylogo.html',d)



def user_joblist(request):
    if not request.user.is_authenticated:
    	return redirect('user_login')
    # user = request.user
    # recruiter = Recruiter.objects.get(user=user)
    # job = Job.objects.filter(recruiter = recruiter)
    # d={'job':job}
    # user = request.user
    # recruiter = Recruiter.objects.get(user=user)
    job = Job.objects.all()
    # recruiter = Recruiter.objects.filter(company=com)
    d={'job':job}
    return render(request,'html/user_joblist.html',d)



def apply_job(request,pid):
	if not request.user.is_authenticated:
		return redirect('user_login')
	error=""
	if request.method == 'POST':
		res = request.FILES['resume']
		st = request.POST['studentname']
		# company= request.POST['company']
		# jt = request.POST['title']
		user = request.user
		job = Job.objects.get(id = pid)
		recruiter = Recruiter.objects.get(job=job)

		try:
			Apply.objects.create(student_resumes=res,applied_student=st,job=job,recruiter=recruiter)
			error="no"
		except:
			error="yes"
	d={'error':error}
	return render(request,'html/apply_job.html',d)




def candidate_applied(request,pid):
	if not request.user.is_authenticated:
		return redirect('recruiter_login')
	# user = request.user
	# recruiter = Recruiter.objects.all()
	# job = Job.objects.filter(recruiter = recruiter)
	app = Apply.objects.filter(job=pid)
	d={'app':app}
	return render(request,'html/candidate_applied.html',d)


