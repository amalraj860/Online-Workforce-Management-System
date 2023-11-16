from django.urls import path, include
from . import views
urlpatterns = [
    path('/login',views.admin_login_fn,name='admin_login'),
    path('',views.admin_home_fn),
    path('logouthr',views.admin_logout,name='logout_admin'),

]
