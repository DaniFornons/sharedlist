from django import forms
from .models import Item, List

class AddItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ["name", "quantity", "notes"]
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Product", "required": True}),
            "quantity": forms.NumberInput(attrs={"min": 1, "value": 1}),
            "notes": forms.TextInput(attrs={"placeholder": "Notes (optional)"}),
        }

class AddListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ["name"]
        widgets = {
            "name": forms.TextInput(attrs={
                "placeholder": "New list name",
                "required": True,
            }),
        }