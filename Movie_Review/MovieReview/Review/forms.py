from .models import Review
from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django import forms 
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['Movie_title', 'Review_Content', 'Rating', 'User ID', 'Created Date']
