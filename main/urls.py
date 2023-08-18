from django.urls import path

from .views import MainBoardView, RenderBoxView

app_name = "main"

urlpatterns = [
    path("", MainBoardView.as_view(), name="board"),
    path("render-box/", RenderBoxView.as_view(), name="render-box"),
]
