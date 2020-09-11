from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.views import View



# class CreateUserView(View):
#     model = User
#     form_class = UserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'register.html'

class RegisterView(View):
    def get(self, request,*args,**kwargs):
        form = UserRegistrationForm
        return render(request, 'register.html', {'form': form})

    def post(self,request,*args,**kwargs):

        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            messages.success(request, f'Konto stworzone dla {email}')
            return redirect('login')

        return render(request, 'register.html',{'form': form})
