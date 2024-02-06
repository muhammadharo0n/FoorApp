from django import forms
from .models import User

class UserForm(forms.ModelForm):
    password= forms.CharField(widget=forms.PasswordInput())
    ConfirmPassword = forms.CharField(widget= forms.PasswordInput())
    class Meta:
        model= User
        fields = ['first_name' ,'last_name','email','phone', 'password','username' ]

    def clean(self):
        cleaned_data = super(UserForm , self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('ConfirmPassword')

        if password != confirm_password:
            raise forms.ValidationError(
                'Password does not match'
            )
        