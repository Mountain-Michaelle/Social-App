from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    #Previous Login url
    #path('login/', views.user_login, name="user_login")
    
    # # Login and Logout using Django Authentication View
    # path('login/', auth_views.LoginView.as_view(), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    # #Password Change views
    # path('password-change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    # path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    
    
    # # password reset
    # path('password-reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    # path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('password-reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('password-reset/complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('profile/<int:profile_id>/', views.profile, name='profile'),
    path('profile/edit/', views.edit, name='edit'),
]
