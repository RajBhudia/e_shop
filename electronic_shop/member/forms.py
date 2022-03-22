from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm

class UserForm(forms.Form):
    USER_TYPE = (
        ('Customer', 'Customer'),
        ('Product', 'Product Admin'),
        ) 
    username = forms.CharField(max_length=50)
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    email = forms.EmailField()
    user_type = forms.ChoiceField(choices=USER_TYPE)



# class Customerform(ModelForm):
#     class Meta:
#         model = Customer
#         fields = ['first_name', 'last_name', 'username', 'password', 'email']