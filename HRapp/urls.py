from django.urls import path, include
from . import views

urlpatterns = [
    path('login',views.hr_login),
    path('',views.hr_home,name='home_hr'),
    path('logouthr',views.hr_logout,name='logout_hr'),
    path('jobposting',views.job_posting_fn,name='hr_jobposting'),
    path('abouthr',views.hr_about,name='about_hr'),
    path('contactshr',views.hr_contactus,name='contacts_hr'),
    path('signup_hr',views.hr_signup,name='signup_hr'),
    path('hr_job_post_history',views.hr_job_history_fn,name='hr_job_History'),
    path('hr_update_profile/',views.hr_profile_updation_fn,name='hr_updates_profile'),
    path('applied_candidate_info/<int:id>',views.view_the_applied_candidate_fn, name='applied_candidate_info'),
    path('download-pdf/<str:id>', views.download_pdf, name='download_pdf'),
]
