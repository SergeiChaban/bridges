from django.urls import path
from django.contrib.auth import views as auth_views
from authapp import views as authapp

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', authapp.register, name='register'),
    path('', authapp.restricted_area, name='restricted_area'),
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    # path('register/', RegisterUserView.as_view(), name='register'),
    # path('login/', UserLoginView.as_view(), name='login'),
    # path('profile/<int:pk>/', UserProfileView.as_view(), name='profile'),
    # path('profile/<int:pk>/', authapp.profile, name='profile'),
    # path('logout/', UserLogoutView.as_view(), name='logout'),
    path('user/company/update/<int:pk>', authapp.company_user_update, name='company_user_update'),
    path('user/profile/update/<int:pk>', authapp.profile_user_update, name='profile_user_update'),
    # path('user/project/update/<int:pk>', authapp.project_user_update, name='project_user_update'),
]
