from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from djuser.models import UserProfileInfo
from django.forms import TextInput, Textarea, FileInput , EmailInput


# for updating user information inside auth_user table
# django gives its default UserChangeForm class which we can call into our class... it is same as UserCreationForm in django used to create new user info
class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
        widgets = {
            'username': TextInput(attrs={'class': 'input', 'placeholder': 'username'}),
            'email': EmailInput(attrs={'class': 'input', 'placeholder': 'email'}),
            'first_name': TextInput(attrs={'class': 'input', 'placeholder': 'first_name'}),
            'last_name': TextInput(attrs={'class': 'input', 'placeholder': 'last_name'}),
        }


# for updating profile information inside djuser_profile table
class UserProfileUpdateForm(forms.ModelForm): 
    class Meta:
        model = UserProfileInfo
        fields = ('phone_no', 'address', 'city',
                  'zip_code', 'country', 'image')
        widgets = {
            'phone': TextInput(attrs={'class': 'input', 'placeholder': 'phone'}),
            'address': TextInput(attrs={'class': 'input', 'placeholder': 'address'}),
            'city': TextInput(attrs={'class': 'input', 'placeholder': 'city'}),
            'zip_code': TextInput(attrs={'class': 'input', 'placeholder': 'zip code'}),
            'country': TextInput(attrs={'class': 'input', 'placeholder': 'country'}),
            'image': FileInput(attrs={'class': 'input', 'placeholder': 'image', }),
        }
