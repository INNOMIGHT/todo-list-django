from django.db.models import (
    Model,
    CharField,
    DateField,
    DateTimeField,
)
from django_extensions.db.fields import AutoSlugField
from django.urls import reverse


class Todo(Model):

    name = CharField(max_length=31)
    slug = AutoSlugField(max_length=31, populate_from=["name"])
    task_date = DateTimeField(auto_now=True)

    class Meta:
        ordering = ["task_date"]

    def get_absolute_url(self):
        return reverse(
            "todo-detail",
            kwargs={
                "slug": self.slug,
            }
        )


