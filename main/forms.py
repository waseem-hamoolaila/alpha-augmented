from typing import Any, Dict
from django import forms

from .models import Session


class RenderBoxForm(forms.Form):
    rows = forms.IntegerField(required=False)
    cols = forms.IntegerField(required=False)

    def clean(self):
        cleaned_data = self.cleaned_data
        rows = cleaned_data.get("rows", None)
        cols = cleaned_data.get("cols", None)

        if not rows or not cols:
            raise forms.ValidationError("Both cols and rows are required to initial new box.")

        if rows > 30 or cols > 30:
            raise forms.ValidationError("30 is the max number for rows/cols")    
        
    def initial_new_session(self):
        rows = self.cleaned_data.get("rows")
        cols = self.cleaned_data.get("cols")

        session = Session.initial_new_box(rows=rows, cols=cols)

        ctx = {
            "box_matrix": session.box_matrix,
            "uuid": session.uuid,
        }

        return ctx


class PlacePackageForm(forms.Form):
    uuid = forms.UUIDField()
    package_id = forms.IntegerField()
    