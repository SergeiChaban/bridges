from django.urls import path

from .views import RegisterUserView, UserLoginView, UserProfileView, UserLogoutView

app_name = 'authapp'

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/<int:pk>/', UserProfileView.as_view(), name='profile'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
]
