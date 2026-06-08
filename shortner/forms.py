from django import forms
from .models import ShortURL

class Form (forms.ModelForm):
    class Meta:
        model = ShortURL
        fields = ['original_url', 'short_key']

        widgets = {
            'original_url' : forms.URLInput(attrs={
                'placeholder' : "https://www.sahilCodes.com"
            }),
            'short_key' : forms.URLInput(attrs={
                'placeholder' : 'Leave blank for auto'
            })
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['short_key'].required = False