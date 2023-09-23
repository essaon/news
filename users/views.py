from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import TemplateView
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.views import PasswordChangeDoneView


class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'registration/password_change_form.html'
    success_url = reverse_lazy('password_change_done')

class CustomChangeDoneView(PasswordChangeDoneView):
    template_name='registration/passwrod_change_done.html'