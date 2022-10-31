from django import forms


class GameForm(forms.Form):
    input = forms.CharField(max_length=3)
