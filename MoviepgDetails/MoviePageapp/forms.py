# forms.py
from django import forms
from .models import Movie, Director

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'year', 'language', 'director']

class DirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = ['name', 'no_movies', 'place']
