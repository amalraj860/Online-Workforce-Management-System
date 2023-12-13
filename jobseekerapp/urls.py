from django.urls import path, include
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin', admin.site.urls),
    path('login', views.jobseeker_login),
    path('', views.jobseeker_home, name='job-seeker_home'),
    path('logout', views.jobseeker_logout, name='logout_jobseeker'),
    path('about', views.about, name='about'),
    path('contact', views.contactus, name='contacts'),
    path('notifications', views.job_listing_fn, name='jobseeker_notification'),
    path('applicationform/<int:id>',views.job_application_form_fn, name='job_applicationform'),
    path('application_history', views.application_history_fn, name='job_applied_history'),
    path('appplicant_profile_update', views.job_seeker_profile_updation_fn, name='applicant_profile_updation'),
    path('signup', views.job_seeker_signup, name='signup_signup'),
    path('forgot_password/',views.forgot_password,name='forgotten_password')
]
