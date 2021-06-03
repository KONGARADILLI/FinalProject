from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class StudentUser(models.Model):
	user =models.ForeignKey(User,on_delete=models.CASCADE)
	mobile = models.CharField(max_length=10,null=True)
	image= models.FileField(null=True)
	gender=models.CharField(max_length=10,null=True)
	type = models.CharField(max_length=10,null=True)
	def _str_(self):
		return self.user.username



class Recruiter(models.Model):
	user =models.ForeignKey(User,on_delete=models.CASCADE)
	mobile = models.CharField(max_length=10,null=True)
	image= models.FileField(null=True)
	gender=models.CharField(max_length=10,null=True)
	company = models.CharField(max_length=100,null=True)
	type = models.CharField(max_length=10,null=True)
	status = models.CharField(max_length=20,null=True)
	def _str_(self):
		return self.user.username

class Job(models.Model):
	recruiter =models.ForeignKey(Recruiter,on_delete=models.CASCADE)
	start_date = models.DateField()
	end_date = models.DateField()
	title =models.CharField(max_length=100)
	salary = models.FloatField(null=True)
	image = models.FileField()
	description = models.CharField(max_length=300)
	experience = models.CharField(max_length=50)
	location = models.CharField(max_length=100)
	skills = models.CharField(max_length=100)
	creationdate = models.DateField()
	

	def str(self):
		return self.title

class Apply(models.Model):
	job = models.ForeignKey(Job,on_delete=models.CASCADE)
	recruiter =models.ForeignKey(Recruiter,on_delete=models.CASCADE)
	student_resumes = models.FileField(null=True)
	applied_student = models.CharField(max_length=20,null=True)
