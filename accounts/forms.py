from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Company


class BaseUserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            "password1",
            "password2",
        ]


class NormalUserRegisterForm(BaseUserRegisterForm):
    """
    No extra fields for normal user.
    """
    pass


class HRUserRegisterForm(BaseUserRegisterForm):
    """
    HR user must provide company info.
    """
    company_name = forms.CharField(max_length=255)
    company_address = forms.CharField(max_length=255, required=False)

    def clean_company_name(self):
        name = self.cleaned_data.get("company_name")
        if not name:
            raise forms.ValidationError("Company name is required for HR users.")
        return name

    def save(self, commit=True):
        # Keep default user creation behaviour; company handled in view.
        user = super().save(commit=commit)
        return user