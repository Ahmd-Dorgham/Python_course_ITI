from django import forms
from .models import Book
from .models import Category

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'desc', 'rate', 'categories']
        widgets = {
            'categories': forms.CheckboxSelectMultiple(),
        }