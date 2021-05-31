from django.urls import path
from OnlinejobportalApp import views

urlpatterns= [

 path('',views.index,name='index'),
 path('admin_login/',views.admin_login,name='admin_login'),
 path('user_login/',views.user_login,name='user_login'),
 path('recruiter_login/',views.recruiter_login,name='recruiter_login'),
 path('user_signup/',views.user_signup,name='user_signup'),
 path('recruiter_signup/',views.recruiter_signup,name='recruiter_signup'),
 path('user_home/',views.user_home,name='user_home'),
 path('recruiter_home/',views.recruiter_home,name='recruiter_home'),
 path('admin_home/',views.admin_home,name='admin_home'),
 path('Logout',views.Logout,name="Logout"),
 path('view_users/',views.view_users,name='view_users'),
 path('recruiter_pending/',views.recruiter_pending,name='recruiter_pending'),
 path('delete_user/<int:pid>',views.delete_user,name='delete_user'),
 path('change_status/<int:pid>',views.change_status,name='change_status'),
 path('recruiter_accepted/',views.recruiter_accepted,name='recruiter_accepted'),
 path('recruiter_rejected/',views.recruiter_rejected,name='recruiter_rejected'),
 path('recruiter_all/',views.recruiter_all,name='recruiter_all'),
 path('delete_recruiter/<int:pid>',views.delete_recruiter,name='delete_recruiter'),
 path('change_passwordadmin/',views.change_passwordadmin,name='change_passwordadmin'),
 path('change_passworduser/',views.change_passworduser,name="change_passworduser"),
 path('change_passwordrecruiter/',views.change_passwordrecruiter,name="change_passwordrecruiter"),
 path('add_job/',views.add_job,name="add_job"),
 path('job_list/',views.job_list,name="job_list"),


]