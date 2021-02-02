from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Todo


class TodoSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = Todo
        fields = "__all__"
        extra_kwargs = {
            "lookup_field": "slug",
            "view_name": "todo-api-detail"
        }
