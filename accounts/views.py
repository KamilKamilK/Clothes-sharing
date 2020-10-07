from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import DetailView

from .forms import UserRegistrationForm, LoginForm

User = get_user_model()

# class CreateUserView(View):
#     model = User
#     form_class = UserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'register.html'

class RegisterView(View):
    def get(self, request, *args, **kwargs):
        form = UserRegistrationForm
        return render(request, 'register.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Konto stworzone dla {username}')
            return redirect('login')

        return render(request, 'register.html', {'form': form})

class LoginView(View):
    form_class = LoginForm
    template_name = 'accounts/login.html'



class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = User
    template_name = "profile_view.html"

    def get_object(self, **kwargs):
        id_ = self.request.user.id
        return get_object_or_404(User, pk=id_)
