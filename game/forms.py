from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from .models import *
from django.forms.widgets import RadioSelect,TextInput
from cloudinary.forms import CloudinaryFileField
#custom form where we can add our own field


class CreateUserForm(UserCreationForm):

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

class DesignForm(forms.ModelForm):
    class Meta:
        model = Design
        exclude = ('owner','price',)

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['color'].queryset = Color.objects.none()

        if 'item' in self.data:
            try:
                item_id = int(self.data.get('item'))
                self.fields['color'].queryset = Color.objects.filter(item_id=item_id).order_by('name')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['color'].queryset = self.instance.item.color_set.order_by('name') 
    

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['size'].queryset = Size.objects.none()


        if 'color' in self.data:
            try:
                color_id = int(self.data.get('color'))
                self.fields['size'].queryset = Size.objects.filter(color_id=color_id).order_by('name')
            except (ValueError,TypeError):
                pass
        elif self.instance.pk:
            self.fields['size'].queryset = self.instance.color.size_set.order_by('name')
