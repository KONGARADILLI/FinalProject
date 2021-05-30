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
 path('admin_home/',views.admin_home,name='admin_home'),
 path('Logout',views.logout,name="Logout"),
 path('view_users/',views.view_users,name='view_users'),
 path('recruiter_pending/',views.recruiter_pending,name='recruiter_pending'),
 path('delete_user/<int:pid>',views.delete_user,name='delete_user'),
 path('change_status/<int:pid>',views.change_status,name='change_status'),

]