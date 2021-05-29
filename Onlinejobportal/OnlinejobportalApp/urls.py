from django.urls import path
from OnlinejobportalApp import views

urlpatterns= [

 path('',views.index,name='index'),
 path('admin_login/',views.admin_login,name='admin_login'),
 path('user_login/',views.user_login,name='user_login'),
 path('recruiter_login/',views.recruiter_login,name='recruiter_login'),
 path('user_signup/',views.user_signup,name='user_signup'),
 path('user_home/',views.user_home,name='user_home'),
]