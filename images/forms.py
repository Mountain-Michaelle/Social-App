from django import forms
from django.core.files.base import ContentFile
from .models import Image
from django.utils.text import slugify
import requests

class ImageCreateForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['title', 'url', 'description']
        widgets = {
            'url': forms.HiddenInput
        }
        
    def clean_url(self):
        url = self.cleaned_data['url']
        valid_extensions = ['jpg', 'png', 'jiff', 'jpeg']
        
        extensions = url.rsplit('.', 1)[1].lower()
        
        if extensions not in valid_extensions:
            raise forms.ValidationError('unsupported image file format')
        
        return url
    
    def save(self, force_insert=False, force_update=False, commit=True):
        
        image = super().save(commit=False)
        image_url = self.cleaned_data['url']
        name = slugify(image.title)
        extension = image_url.rsplit('.', 1)[1].lower()
        image_name = f'{name}.{extension}'
        
        # downloading image from the given url
        response = requests.get(image_url)
        image.image.save(image_name, ContentFile(response.content), save=False)
        
        
        if commit:
            image.save()
        return image