from django import forms
from GenerationCalculator.Apps.Generations.models import Generations

class HomeForm(forms.ModelForm):
    birthyear = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
        }
    ))

    class Meta:
        model = Generations
        #fields = ('name', 'description', 'from_year', 'to_year')
        fields = ()