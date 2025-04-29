from django import forms
from .models import Book

class BookstoreForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name','category','price','status','date']
        widgets = {
            'status':forms.Select(choices=Book.STATUS_CHOCIES),
        }