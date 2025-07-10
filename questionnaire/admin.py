from django.contrib import admin

from questionnaire.models import *


class ClientAdmin(admin.ModelAdmin):
    list_filter = [
        'name',
        'email',
        'state',
        'domain',
    ]

    search_fields = (
        'pk',
        'name',
        'mail',
        'state',
        'domain',
    )


class PremiumWebsiteFormAdmin(admin.ModelAdmin):
    list_filter = [
        'camp',
    ]
    
    search_fields = (
        'pk',
        'camp',
    )


class QandAAdmin(admin.ModelAdmin):
    list_filter = [
        'checked',
        'type',
        'question',
    ]
    
    search_fields = (
        'pk',
        'type',
        'question',
        'answer',
        'checked',
        'questionnaire',
    )


admin.site.register(User, ClientAdmin)
admin.site.register(PremiumWebsiteForm, PremiumWebsiteFormAdmin)
admin.site.register(QandA, QandAAdmin)
