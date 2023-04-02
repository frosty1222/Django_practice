from django import forms

class TaskForm(forms.Form):
    status = forms.BooleanField(required=False)