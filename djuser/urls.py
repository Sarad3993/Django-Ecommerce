from django.urls import path 
from djuser.views import *
from django.contrib.auth import views as auth_views
app_name = 'djuser'

urlpatterns = [
    path('',index, name='index'),
    path('login/',login_form,name ='login'),
    path('logout/',logout_function,name='logout'),
    path('signup/',signup_form,name='signup'),
    path('update_profile/',user_profile_update,name='update_profile'),
    path('change_password/',user_password_change,name='change_password'),

        # for password reset 
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name="password_reset.html"),
         name="password_reset"),

    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name="password_reset_done.html"),
         name="password_reset_done"),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"),
         name="password_reset_confirm"),

    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_complete.html"),
         name="password_reset_complete"),
]
]

