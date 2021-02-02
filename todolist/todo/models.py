from django.db.models import (
    Model,
    CharField,
    DateField,
    DateTimeField,
)
from django_extensions.db.fields import AutoSlugField


class Todo(Model):

    name = CharField(max_length=31)
    slug = AutoSlugField(max_length=31, populate_from=["name"])
    task_date = DateTimeField(auto_now=True)

    class Meta:
        ordering = ["task_date"]


