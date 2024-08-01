from django.urls import path 
from django.contrib.auth import views as auth_views
# from . import views


app_name = 'account'


urlpatterns = [
    #Previous Login url
    #path('login/', views.user_login, name="user_login")
    
    # Login and Logout using Django Authentication View
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout')
]
