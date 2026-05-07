from django import forms
from .models import UnionMeetingInfo


class UnionMeetingInfoForm(forms.ModelForm):
    class Meta:
        model = UnionMeetingInfo
        fields = [
            "meeting_date",
            "location",
            "agenda",
            "past_meeting_notes",
            "union_contacts",
        ]

        widgets = {
            "meeting_date": forms.DateTimeInput(
                attrs={
                    "type": "datetime-local",
                    "class": "form-control",
                }
            ),
            "location": forms.TextInput(attrs={"class": "form-control"}),
            "agenda": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
            "past_meeting_notes": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
            "union_contacts": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
        }