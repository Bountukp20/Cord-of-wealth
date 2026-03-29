from django import forms
from django.db import models
from django.forms import fields
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.core.validators import RegexValidator
from phonenumber_field.formfields import PhoneNumberField


# class SubscribeForm(forms.ModelForm):
#     class Meta:
#         model = Subscriber
#         fields = ['email']

# class NewsletterForm(forms.ModelForm):
#     class Meta:
#         model = Newsletter
#         fields = ['subject', 'content']
#         widgets = {
#             'content': forms.Textarea(attrs={'rows': 5}),
                                                                                            # }

class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(label="username", max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'username12', 'style': 'width: 100%; padding: 12px; border: 1px solid #ccc; border-radius: 4px; box-sizing: border-box; resize: vertical;',
                                                             'class': 'form-control',
                                                                  }))                              
    email = forms.CharField(label="email", max_length=100,
                               required=True,
                               widget=forms.EmailInput(attrs={'placeholder': 'Example12@gmail.com', 'style': 'width: 100%; padding: 12px; border: 1px solid #ccc; border-radius: 4px; box-sizing: border-box; resize: vertical;',
                                                             'class': 'form-control',
                                                                  }))           
    first_name = forms.CharField(label="first_name", max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'John', 'style': 'width: 100%; padding: 12px; border: 1px solid #ccc; border-radius: 4px; box-sizing: border-box; resize: vertical;',
                                                             'class': 'form-control',
                                                                  }))                   
    last_name = forms.CharField(label="last_name", max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Doe', 'style': 'width: 100%; padding: 12px; border: 1px solid #ccc; border-radius: 4px; box-sizing: border-box; resize: vertical;',
                                                             'class': 'form-control',
                                                                  }))                   
    phone = PhoneNumberField(label="phone", region="NG", required=True)                        
                             
    password1 = forms.CharField(label="assword", max_length=15,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'style': 'width: 100%; padding: 12px; border: 1px solid #ccc; border-radius: 4px; box-sizing: border-box; resize: vertical;',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }), validators=[RegexValidator(regex=r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$', message="Password must be at least 8 characters long and include a letter, a number, and a special character")],)       
    password2 = forms.CharField(label="confirm", max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password', 'style': 'width: 100%; padding: 12px; border: 1px solid #ccc; border-radius: 4px; box-sizing: border-box; resize: vertical;',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))

    class Meta:
        model = User
        fields = ['username', 'email', 'phone', 'password1', 'password2']
        
                                                                
class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Email", widget=forms.EmailInput(attrs={'class':'email-input'}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'id':'password-input'}))
    
    class Meta:
            model = User
            fields = ['username', 'password']

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('confirm')

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('This account is already created.')
        if password2!=password:
            raise forms.ValidationError("Password does not match.")
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('This user does not exist, please <a href="/sign up">register</a>')
            if not user.check_password(password):
                raise forms.ValidationError('You have entered the wrong password. <a href="#">Did you forget your password?</a>')
            if not user.is_active:
                raise forms.ValidationError('This account is not active. Please <a href="#">contact support</a>')
            return super(LoginForm, self).clean(*args, **kwargs)
        return username
    