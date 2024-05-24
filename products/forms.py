from django import forms
from .widgets import CustomClearableFileInput
from .models import Thing, Category, Instructions
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class ProductForm(forms.ModelForm):

    class Meta:
        model = Thing
        fields = '__all__'

    featured_image = forms.ImageField(label='Featured_Image', required=False, widget=CustomClearableFileInput)

    description = forms.CharField(widget=SummernoteWidget())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-2'
