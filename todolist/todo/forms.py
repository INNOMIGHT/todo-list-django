from django.forms import ModelForm
from .models import Todo


class LowerCaseNameMixin:

    def clean_name(self):
        return self.cleaned_data['name']


class SlugCleanMixin:

    def clean_slug(self):
        return self.cleaned_data["slug"]


class TodoForm(ModelForm, LowerCaseNameMixin, SlugCleanMixin):

    class Meta:
        model = Todo
        fields = "__all__"



