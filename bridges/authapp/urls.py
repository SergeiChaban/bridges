from django.urls import path
# from .views import RegisterUserView, UserLoginView, UserProfileView, UserLogoutView
from .views import RegisterUserView, UserLoginView, UserLogoutView
from authapp import views as authapp

app_name = 'authapp'

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    # path('profile/<int:pk>/', UserProfileView.as_view(), name='profile'),
    path('profile/<int:pk>/', authapp.profile, name='profile'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('user/company/update/<int:pk>', authapp.company_users_update, name='company_users_update'),
    path('user/profile/update/<int:pk>', authapp.profile_user_update, name='profile_user_update'),
]
