from typing import Any, Dict
from django import forms

from .models import Session
from processor.helpers import get_package_from_list


class RenderBoxForm(forms.Form):
    rows = forms.IntegerField(required=False)
    cols = forms.IntegerField(required=False)

    def clean(self):
        cleaned_data = self.cleaned_data
        rows = cleaned_data.get("rows", None)
        cols = cleaned_data.get("cols", None)

        if not rows or not cols:
            raise forms.ValidationError("Both cols and rows are required to initial new box.")

        if rows > 20 or cols > 20:
            raise forms.ValidationError("20 is the max number for rows/cols")

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
    rotation = forms.BooleanField(required=False)
    rtl = forms.BooleanField(required=False)
    vertical = forms.BooleanField(required=False)

    session = None

    def clean(self):
        cleaned_data = self.cleaned_data

        uuid = cleaned_data.get("uuid")
        package_id = cleaned_data.get("package_id")

        if not uuid:
            raise forms.ValidationError("UUID is required, Please create a box and try again.")

        try:
            self.session = Session.objects.get(uuid=uuid)
        except:
            raise forms.ValidationError("UUID is not valid.")

        if not get_package_from_list(identifier=package_id):
            raise forms.ValidationError("Package id is not valid.")

    def place(self):
        rotation = self.cleaned_data.get("rotation")
        rtl = self.cleaned_data.get("rtl")
        vertical = self.cleaned_data.get("vertical")
        
        result, new_matrix = self.session.place_package(self.cleaned_data.get("package_id"), rotation=rotation, rtl=rtl)

        ctx = {
            "result": result,
            "box_matrix": new_matrix,
            "uuid": self.cleaned_data.get("uuid"),
        }

        return ctx
