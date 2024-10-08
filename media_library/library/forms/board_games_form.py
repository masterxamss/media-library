from django import forms
from library.models import BoardGame


class BoardGameForm(forms.ModelForm):
    class Meta:
        model = BoardGame
        fields = '__all__'
        exclude = ['slug']
        labels = {
            'name': 'Nom',
            'creator': 'Créateur',
            'description': 'Description'
        }
        error_messages = {
            'name': {
                'required': 'Veuillez renseigner le nom',
                'max_length': 'Limite de caractères dépassée'
            },
            'creator': {
                'required': 'Veuillez renseigner le créateur',
                'max_length': 'Limite de caractères dépassée'
            },
            'description': {
                'max_length': 'Limite de caractères dépassée'
            },
            'image': {
                'filename': 'Veuillez insérer une image valide',
                'error_type': 'format non valide',
            }
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Nom du jeu', 'class': 'form-control'}),
            'creator': forms.TextInput(attrs={'placeholder': 'Nom du créateur', 'class': 'form-control'}),
            'description': forms.Textarea(attrs={'placeholder': 'Description', 'class': 'form-control'}),
            'image': forms.FileInput(attrs={'placeholder': 'Image', 'class': 'form-control'})
        }
