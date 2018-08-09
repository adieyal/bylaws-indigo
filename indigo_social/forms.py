from django.forms import ModelForm
from django.contrib.auth.models import User

from indigo_app.models import Editor


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')


class UserProfileForm(ModelForm):
    class Meta:
        model = Editor
        fields = ('country',)
