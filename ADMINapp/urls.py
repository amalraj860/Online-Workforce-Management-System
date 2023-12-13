from django.urls import path, include
from . import views
urlpatterns = [
    path('/login',views.admin_login_fn,name='admin_login'),
    path('',views.admin_home_fn),
    path('admin/jobseeker',views.admin_jobseeker_home_fn,name='admin_job_seeker_home'),
    path('admin/hr', views.admin_hr_home_fn, name='admin_hr_home'),
    path('jobseeker/signup', views.admin_jobseeker_add_fn, name='admin_jobseeker_signup'),
    path('hr/signup', views.admin_hr_add_fn, name='admin_hr_signup'),
    path('/show', views.admin_jobseeker_show_fn,name='jobseeker_show'),
    path('/update/<str:id>', views.admin_jobseeker_update_fn, name="update_jobseeker"),
    path('/delete/<str:id>', views.admin_jobseeker_delete_fn, name="delete_jobseeker"),
    path('/jobview/<str:id>',views.admin_jobseeker_jobview_fn,name='job_view'),
    path('/hr_show',views.admin_hr_show_fn,name='hr_show'),
    path('/hr_update/<str:id>', views.admin_hr_update_fn, name="update_hr"),
    path('/job_posting/<str:id>',views.admin_hr_jobposting_details_fn,name='hr_job_view'),
    path('/admin_job_candidate/<str:id>', views.admin_hr_job_candidate_details_fn, name='candidate_dtls'),
    path('/hr_delete/<str:id>', views.admin_hr_delete_fn, name="delete_hr"),
    path('/dashboard',views.admin_jobseeker_count_fn,name="dashboard"),
    path('logoutadmin',views.admin_logout,name='logout_admin'),

]
