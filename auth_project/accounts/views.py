# accounts/views.py
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Successfully logged in.")
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# accounts/views.py
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserCreationForm

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            backend_str = 'accounts.backends.EmailOrUsernameBackend'  # Use this backend path
            login(request, user, backend=backend_str)
            messages.success(request, "Account created successfully. You are now logged in.")
            return redirect('dashboard')
        else:
            messages.error(request, "There was an error with your sign-up. Please correct the errors below.")
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})


# accounts/views.py
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomPasswordChangeForm

@login_required
def change_password(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            from django.contrib.auth import update_session_auth_hash
            update_session_auth_hash(request, user)  # Important! Keeps the user logged in
            messages.success(request, 'Your password was successfully updated!')
            return redirect('dashboard')
        else:
            messages.error(request, 'There was an error changing your password. Please correct the errors below.')
    else:
        form = CustomPasswordChangeForm(request.user)
    return render(request, 'change_password.html', {'form': form})


# accounts/views.py
@login_required
def dashboard(request):
    return render(request, 'dashboard.html', {'user': request.user})

from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib import messages

def custom_logout_view(request):
    logout(request)
    messages.success(request, "Successfully logged out.")
    return redirect('login')

# accounts/views.py
@login_required
def profile(request):
    return render(request, 'profile.html', {
        'user': request.user,
    })

from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.contrib.auth.models import User
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import CustomPasswordResetForm

class CustomPasswordResetView(auth_views.PasswordResetView):
    template_name = 'password_reset.html'
    email_template_name = 'password_reset_email.html'
    form_class = CustomPasswordResetForm
    success_url = reverse_lazy('password_reset_done')

    def form_valid(self, form):
        email = form.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            return super().form_valid(form)
        else:
            messages.error(self.request, "There is no user registered with the specified email address.")
            return self.form_invalid(form)


class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'password_reset_done.html'

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'password_reset_confirm.html'
    success_url = reverse_lazy('password_reset_complete')

class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'password_reset_complete.html'

from django.shortcuts import redirect

def root_redirect(request):
    return redirect('login')
