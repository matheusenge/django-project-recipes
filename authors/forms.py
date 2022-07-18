from django import forms
from django.contrib.auth.models import User


def add_attr(field, attr_name, attr_new_val):
    existing_attr = field.widget.attrs.get(attr_name, '')
    field.widget.attrs[attr_name] = f'{existing_attr} {attr_new_val}'.strip()


def add_placeholder(field, placeholder_val):
    add_attr(field, 'placeholder', placeholder_val)


class RegisterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_placeholder(self.fields['username'], 'Your username')
        add_placeholder(self.fields['email'], 'Your E-mail')
        add_placeholder(self.fields['first_name'], 'Ex.: Matheus')
        add_placeholder(self.fields['last_name'], 'Ex.: Enge')
        add_placeholder(self.fields['password'], 'Your password')
        add_placeholder(
            self.fields['confirm_password'], 'Repeat your password')

    confirm_password = forms.CharField(
        required=True, widget=forms.PasswordInput, label='Confirm Password')

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput
        }
