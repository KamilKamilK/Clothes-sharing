from django.urls import path, include
from accounts import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('registration/', views.RegisterView.as_view(), name='registration'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),

]