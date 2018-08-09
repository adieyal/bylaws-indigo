from django.contrib.auth.models import User
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse
from django.views.generic import DetailView, FormView

from indigo_social.forms import UserProfileForm, UserForm


class UserProfileView(DetailView):
    queryset = User.objects
    context_object_name = 'user'


class EditAccountView(FormView):
    template_name = 'indigo_social/account/edit.html'
    form_class = UserForm

    def get_success_url(self):
        return reverse('indigo_social:edit_account')

    def get_form_kwargs(self):
        kwargs = super(EditAccountView, self).get_form_kwargs()
        kwargs['instance'] = self.request.user
        return kwargs

    def form_valid(self, form):
        self.object = form.save()
        return super(EditAccountView, self).form_valid(form)
