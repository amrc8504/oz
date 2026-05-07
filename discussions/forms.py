from django import forms
from .models import DiscussionPost, DiscussionComment
from website.moderation import contains_banned_words


class DiscussionPostForm(forms.ModelForm):
    class Meta:
        model = DiscussionPost
        fields = ["title", "content"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "content": forms.Textarea(attrs={"class": "form-control", "rows": 6}),
        }

    def clean_title(self):
        title = self.cleaned_data.get("title")

        if contains_banned_words(title):
            raise forms.ValidationError("This title contains inappropriate language.")

        return title

    def clean_content(self):
        content = self.cleaned_data.get("content")

        if contains_banned_words(content):
            raise forms.ValidationError("This post contains inappropriate language.")

        return content


class DiscussionCommentForm(forms.ModelForm):
    class Meta:
        model = DiscussionComment
        fields = ["content"]
        widgets = {
            "content": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
        }

    def clean_content(self):
        content = self.cleaned_data.get("content")

        if contains_banned_words(content):
            raise forms.ValidationError("This comment contains inappropriate language.")

        return content