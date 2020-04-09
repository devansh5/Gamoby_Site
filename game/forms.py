from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from .models import Profile
from django.forms.widgets import RadioSelect

#custom form where we can add our own field


class CreateUserForm(UserCreationForm):
    email = forms.EmailField(max_length=200)

    class meta:
        model = User
        fields = (
            'email',
            'username',
            'password1',
            'password2')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
            
    
        
class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
        )


class ProfileUpdate(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
            'gender',
            'address1',
            'address2',
            'city',
            'state',
            'pin',
            'country',
            'mobileno',
        )
        widgets = {
            'gender':forms.RadioSelect()
        }