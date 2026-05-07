from django import forms
from .models import Announcement
from website.moderation import contains_banned_words


class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ["title", "content"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "content": forms.Textarea(attrs={"class": "form-control", "rows": 5}),
        }

    def clean_title(self):
        title = self.cleaned_data.get("title")

        if contains_banned_words(title):
            raise forms.ValidationError("This title contains inappropriate language.")

        return title

    def clean_content(self):
        content = self.cleaned_data.get("content")

        if contains_banned_words(content):
            raise forms.ValidationError("This announcement contains inappropriate language.")

        return content