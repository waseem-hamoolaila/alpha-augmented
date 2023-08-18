from typing import Any, Dict
from django import forms

from .models import Session


class RenderBoxForm(forms.Form):
    uuid = forms.UUIDField(required=False)
    rows = forms.IntegerField(required=False)
    cols = forms.IntegerField(required=False)

    is_new = False

    def clean(self):
        cleaned_data = self.cleaned_data
        uuid = cleaned_data.get("uuid", None)
        rows = cleaned_data.get("rows", None)
        cols = cleaned_data.get("cols", None)

        self.is_new = True if uuid else False

        if not rows or not cols:
            raise forms.ValidationError("Both cols and rows are required to initial new box.")

    def initial_new_session(self):
        rows = self.cleaned_data.get("rows")
        cols = self.cleaned_data.get("cols")

        session = Session.initial_new_box(rows=rows, cols=cols)

        ctx = {
            "box_matrix": session.box_matrix,
            "uuid": session.uuid,
        }

        return ctx
