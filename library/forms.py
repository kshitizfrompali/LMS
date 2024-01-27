from django import forms
from django.contrib.auth.models import User
from . import models
# from .models import *

class ContactusForm(forms.Form):
    Name = forms.CharField(max_length=30)
    Email = forms.EmailField()
    Message = forms.CharField(max_length=500,widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))




class AdminSigupForm(forms.ModelForm):
    
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'first_name','placeholder':'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'last_name','placeholder':'Last Name'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'id': 'username','placeholder':'Username'}),
            'password': forms.TextInput(attrs={'class': 'form-control', 'id': 'password','placeholder':'Password'}),
        }
        


class StudentUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'first_name','placeholder':'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'last_name','placeholder':'Last Name'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'id': 'username','placeholder':'Username'}),
            'password': forms.TextInput(attrs={'class': 'form-control', 'id': 'password','placeholder':'Password'}),
        }

class StudentExtraForm(forms.ModelForm):
    class Meta:
        model=models.StudentExtra
        fields=['enrollment','branch']
        widgets = {
            'enrollment': forms.TextInput(attrs={'class': 'form-control', 'id': 'enrollment','placeholder':'Enrollment'}),
            'branch': forms.TextInput(attrs={'class': 'form-control', 'id': 'branch','placeholder':'Branch'}),
        }

class BookForm(forms.ModelForm):
    class Meta:
        model=models.Book
        fields=['name','isbn','author','category']
class IssuedBookForm(forms.Form):
    #to_field_name value will be stored when form is submitted.....__str__ method of book model will be shown there in html
    isbn2=forms.ModelChoiceField(queryset=models.Book.objects.all(),empty_label="Name and isbn", to_field_name="isbn",label='Name and Isbn')
    enrollment2=forms.ModelChoiceField(queryset=models.StudentExtra.objects.all(),empty_label="Name and enrollment",to_field_name='user',label='Name and enrollment')

