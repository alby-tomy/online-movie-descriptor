from django import forms
from .models import MovieDetails

class MovieForm(forms.ModelForm):
    class Meta:
        model = MovieDetails
        fields = ['name','description','year','img']