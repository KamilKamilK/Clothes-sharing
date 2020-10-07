from django.urls import path
from accounts import views
from django.contrib.auth import views as auth_views
from charity.views import AjaxView
from accounts.views import ProfileDetailView



urlpatterns = [
    path('registration/', views.RegisterView.as_view(), name='registration'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path("ajax/", AjaxView.as_view(), name="ajax"),
    path("profil/", ProfileDetailView.as_view(), name="profile"),
]