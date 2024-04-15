# accounts/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

# 만약 추가적인 로그인 폼 커스터마이징이 필요하다면
class LoginForm(AuthenticationForm):
    # 필요한 커스텀 필드를 추가
    pass
