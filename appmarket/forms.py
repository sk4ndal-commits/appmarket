from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password


class RegistrationForm(forms.Form):
    email = forms.EmailField(label='Email', required=True)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput, required=True)

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('A user with that email already exists.')
        return email

    def clean(self):
        cleaned = super().clean()
        p1 = cleaned.get('password1')
        p2 = cleaned.get('password2')
        if p1 and p2 and p1 != p2:
            self.add_error('password2', 'Passwords do not match.')
        # validate password strength
        if p1:
            try:
                validate_password(p1)
            except forms.ValidationError as e:
                self.add_error('password1', e.messages[0])
        return cleaned

    def save(self):
        data = self.cleaned_data
        user = User.objects.create_user(username=data['email'], email=data['email'], password=data['password1'])
        return user
