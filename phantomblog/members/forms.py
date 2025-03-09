from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.password_validation import validate_password
from django.forms import ValidationError


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
        labels = {
            'first_name': '',
            'last_name': '',
            'username': '',
            'email': '',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'First name'}),
            'last_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last name'}),
            'username': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username'}),
            'email': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add Bootstrap classes to password fields
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Password'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Confirm Password'
        })
        
        # Remove help texts
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''

        # Proper error class handling
        for field_name, field in self.fields.items():
            if field_name in self.errors:  # Check errors using field_name
                field.widget.attrs.update({
                    'class': f'{field.widget.attrs.get("class", "")} is-invalid'
                })


# Create a form for the Profile model
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_pic', 'location', 'bio', 'facebook_link', 'tiktok_link', 'instagram_link', 'x_link', 'linkedin_link', 'github_link']
        labels = {
            'profile_pic': '',
            'bio': '',
            'location': '',
            'facebook_link': '',
            'tiktok_link': '',
            'instagram_link': '',
            'x_link': '',
            'linkedin_link': '',
            'github_link': '',
        }
        widgets = {
            'profile_pic': forms.FileInput(attrs={'class': 'btn btn-outline-secondary buttons smaller-btn'}),
            'bio': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Bio'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Country/Location'}),
            'facebook_link': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Your facebook account link'}),
            'tiktok_link': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Your tiktok account link'}),
            'instagram_link': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Your instagram account link'}),
            'x_link': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Your X account link'}),
            'linkedin_link': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Your linkedin account link'}),
            'github_link': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Your github account link'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # If the user is not a writer, hide the social fields
        if not self.instance.is_writer:
            for field in ['facebook_link', 'tiktok_link', 'instagram_link', 'x_link', 'linkedin_link', 'github_link']:
                self.fields[field].widget = forms.HiddenInput()

# Create a form to handle user
class UserForm(forms.ModelForm):
    password1 = forms.CharField(
        label="",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'New Password'
        }),
        required=False,
        help_text="Leave blank to keep the current password."
    )
    password2 = forms.CharField(
        label="",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirm New Password'
        }),
        required=False,
        help_text="Enter the same password as above for verification."
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']
        labels = {
            'first_name': 'First name',
            'last_name': 'Last name',
            'username': 'Username',
            'email': 'Email'
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add error classes and preserve help texts
        for field_name, field in self.fields.items():
            # Add Bootstrap error class
            if field_name in self.errors:
                field.widget.attrs.update({
                    'class': f'{field.widget.attrs.get("class", "")} is-invalid'
                })

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 or password2:
            if password1 != password2:
                self.add_error('password2', "Passwords do not match.")
            else:
                try:
                    validate_password(password1, self.instance)
                except ValidationError as e:
                    self.add_error('password1', e)

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        if password := self.cleaned_data.get('password1'):
            user.set_password(password)
        if commit:
            user.save()
        return user