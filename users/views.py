from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import TemplateView
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.views import PasswordChangeDoneView
from django.contrib.auth.views import LogoutView, LoginView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView


class logout_view(LogoutView):
    success_url = reverse_lazy('home')

class login_view(LoginView):
    template_name = 'registration/login.html'

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'password_change_form.html'
    success_url = reverse_lazy('password_change_done')

class CustomChangeDoneView(PasswordChangeDoneView):
    template_name='password_change_done.html'

class CustomPassResetView(PasswordResetView):
    template_name = 'password_reset_form.html'
    success_url = reverse_lazy('password_reset_done')
class CustomPassResetConfirmView(PasswordResetConfirmView):
    template_name = 'password_reset_confirm.html'
class CustomPassResetCompleteView(PasswordResetCompleteView):
    template_name = 'password_reset_complete.html'
class CustomPassResetDoneView(PasswordResetDoneView):
    template_name = 'password_reset_done.html'