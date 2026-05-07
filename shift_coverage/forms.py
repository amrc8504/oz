from django import forms
from .models import ShiftCoveragePost


class ShiftCoveragePostForm(forms.ModelForm):

    class Meta:
        model = ShiftCoveragePost

        fields = [
            "title",
            "shift_date",
            "start_time",
            "end_time",
            "location",
            "note",
        ]

        widgets = {
            "title": forms.TextInput(attrs={
                "class": "form-control"
            }),

            "shift_date": forms.DateInput(attrs={
                "type": "date",
                "class": "form-control"
            }),

            "start_time": forms.TimeInput(attrs={
                "type": "time",
                "class": "form-control"
            }),

            "end_time": forms.TimeInput(attrs={
                "type": "time",
                "class": "form-control"
            }),

            "location": forms.TextInput(attrs={
                "class": "form-control"
            }),

            "note": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 4
            }),
        }