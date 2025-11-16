from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Feature, Todo, SuggestedFeature


class FeatureForm(forms.ModelForm):
    """Form for adding/editing features in admin"""
    class Meta:
        model = Feature
        fields = ['title', 'description', 'icon_svg', 'order', 'is_active']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Feature title',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-textarea',
                'placeholder': 'Feature description',
                'rows': 4,
            }),
            'icon_svg': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Icon name or SVG',
            }),
            'order': forms.NumberInput(attrs={
                'class': 'form-input',
                'type': 'number',
            }),
        }


class CustomUserCreationForm(UserCreationForm):
    """Professional user registration form"""
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-input',
            'placeholder': 'Email address',
            'autocomplete': 'email',
        })
    )
    first_name = forms.CharField(
        max_length=30,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'First name',
        })
    )
    last_name = forms.CharField(
        max_length=150,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'Last name',
        })
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-input',
            'placeholder': 'Username',
            'autocomplete': 'username',
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'form-input',
            'placeholder': 'Password',
            'autocomplete': 'new-password',
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-input',
            'placeholder': 'Confirm password',
            'autocomplete': 'new-password',
        })

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already registered.")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class CustomAuthenticationForm(AuthenticationForm):
    """Professional login form"""
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'Username or email',
            'autocomplete': 'username',
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-input',
            'placeholder': 'Password',
            'autocomplete': 'current-password',
        })
    )


class TodoForm(forms.ModelForm):
    """Form for creating/editing todos"""
    class Meta:
        model = Todo
        fields = ['title', 'description', 'priority', 'status', 'due_date']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Task title',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-textarea',
                'placeholder': 'Task description',
                'rows': 4,
            }),
            'priority': forms.Select(attrs={
                'class': 'form-select',
            }),
            'status': forms.Select(attrs={
                'class': 'form-select',
            }),
            'due_date': forms.DateTimeInput(attrs={
                'class': 'form-input',
                'type': 'datetime-local',
            }),
        }


class SuggestedFeatureForm(forms.ModelForm):
    """Form for users to suggest features"""
    class Meta:
        model = SuggestedFeature
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Feature title',
                'maxlength': '200',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-textarea',
                'placeholder': 'Describe your feature idea...',
                'rows': 5,
            }),
        }
