from django.urls import path

from .views import MainBoardView, RenderBoxView, PlacePackageView

app_name = "main"

urlpatterns = [
    path("", MainBoardView.as_view(), name="board"),
    path("render-box/", RenderBoxView.as_view(), name="render-box"),
    path("place-package/", PlacePackageView.as_view(), name="place-package"),
]
