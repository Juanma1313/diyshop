from django.contrib import admin
from .models import UserProfile
# Register your models here.


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    ''' Handles user profiles in admin pages'''

    list_display = ('user',)

    fields = (
        'user',
        'default_phone_number',
        'default_street_address1',
        'default_street_address2',
        'default_town_or_city',
        'default_county',
        'default_postcode',
        'default_country',
    )

    search_fields = (
        'user',
        'default_phone_number',
        'default_street_address1',
        'default_street_address2',
        'default_town_or_city',
        'default_county',
        'default_postcode',
        'default_country',
    )

    list_filter = (
        'default_postcode',
        'default_country',
    )

    ordering = ('user',)

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['user'].widget.can_change_related = False
        form.base_fields['user'].widget.can_add_related = False
        return form
