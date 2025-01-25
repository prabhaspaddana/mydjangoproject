from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm, PasswordChangeForm

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("A user with this email already exists.")
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("A user with this username already exists.")
        return username

class CustomPasswordResetForm(PasswordResetForm):
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError("There is no user registered with the specified email address.")
        return email


from django.contrib.auth import get_user_model

UserModel = get_user_model()

class CustomPasswordChangeForm(PasswordChangeForm):
    def clean_new_password1(self):
        new_password = self.cleaned_data.get('new_password1')
        old_password = self.cleaned_data.get('old_password')
        
        if new_password == old_password:
            raise forms.ValidationError("The new password cannot be the same as the old password.")
        return new_password
