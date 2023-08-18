from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, FormView
from django.http import JsonResponse

from .forms import RenderBoxForm


class MainBoardView(TemplateView):
    template_name = "main/main_board.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class RenderBoxView(FormView):
    """
    A view to render existing or new box.

    NOTE: used it as a normal view and form only for the ease of the demo
    the best solution will be to use DRF and serializers.
    """

    form_class = RenderBoxForm
    template_name = "main/main_board.html"

    def form_valid(self, form):
        super().form_valid(form)

        return JsonResponse({}, status=200)

    def form_invalid(self, form):
        super().form_invalid(form)

        return JsonResponse({}, status=400)
