from .models import Review, CustomUser
from django import forms 
from django.contrib.auth.forms import UserCreationForm

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['Movie_title', 'Review_Content', 'Rating', 'User ID', 'Created Date']

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)