from typing import Any, Dict
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView


class MainBoardView(TemplateView):
    template_name = "main/main_board.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        return context
