from django import forms
from .widgets import CustomClearableFileInput
from .models import Thing, Category, Instructions
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django.core.handlers.wsgi import WSGIRequest


class ProductForm(forms.ModelForm):

    class Meta:
        model = Thing
        fields = '__all__'

    featured_image = forms.ImageField(
        label='Featured_Image',
        required=False,
        widget=CustomClearableFileInput)

    description = forms.CharField(widget=SummernoteWidget())

    def __init__(self, *args, **kwargs):
        # Search for request parameter and eliminate it for the parent class
        request = None
        try:
            request = kwargs.pop('request')
        except Exception:
            request = None

        super().__init__(*args, **kwargs)

        if request:
            #  User checking and default author
            user = request.user
            if user.is_authenticated:
                # User is a registered, author is user
                self.fields['author'].initial = user
            if not user.is_superuser and not user.is_staff:
                # User is a regular user, cannot change author
                self.fields['author'].disabled = True
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-2'
