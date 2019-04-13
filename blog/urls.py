from django.urls import path
from . import views
app_name = 'blog'
urlpatterns = [
    path("",views.index, name="index"),
    path("post/<int:id>", views.get_post),
    path("greet/<name>", views.greet),
    path("jokes/create", views.JokeCreateView.as_view(), name="create_joke"),
    path("jokes/list", views.JokeListView.as_view(), name="list_joke"),
]
