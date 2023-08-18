from django.urls import path

from .views import MainBoardView

app_name = "main"

urlpatterns = [
    path("", MainBoardView.as_view(), name="board"),
]
