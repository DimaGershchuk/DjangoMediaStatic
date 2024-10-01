from .models import MyMedia
from django.contrib.auth.forms import forms


class MediaForm(forms.ModelForm):
    class Meta:
        model = MyMedia
        fields = ['title', 'file', 'image']

        widgets = {
            'file': forms.FileInput(attrs={'accept': '.txt, .pdf, .docx'}),
            'image': forms.FileInput(attrs={'accept': '.png, .jpg, .jpeg'})
        }

