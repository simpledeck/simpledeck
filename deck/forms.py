from typing import List

from django import forms

from .models import Deck


class CreateForm(forms.Form):
    title = forms.CharField(label="Title", max_length=2048)
    text = forms.CharField(required=False, widget=forms.HiddenInput)
    theme = forms.ChoiceField(choices=Deck.THEMES, widget=forms.Select)


class DeleteForm(forms.ModelForm):
    class Meta:
        model = Deck
        fields: List[str] = []
