from django.forms import ModelForm
from django.contrib.auth.models import User
from captcha.fields import ReCaptchaField
from allauth.account.forms import SignupForm

from indigo_app.models import Editor


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')


class UserProfileForm(ModelForm):
    class Meta:
        model = Editor
        fields = ('country',)


class UserSignupForm(SignupForm):
    captcha = ReCaptchaField()
