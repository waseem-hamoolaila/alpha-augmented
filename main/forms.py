from django import forms


class RenderBoxForm(forms.Form):
    uuid = forms.UUIDField(required=False)
    rows = forms.IntegerField(required=False)
    cols = forms.IntegerField(required=False)
