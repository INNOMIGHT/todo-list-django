from rest_framework.routers import SimpleRouter
from .viewsets import TodoViewSet


api_routes = SimpleRouter()
api_routes.register("todo", TodoViewSet, basename="todo-api")

api_router = api_routes.urls

urlpatterns = api_router
