from django.contrib import admin

from .models import ClientSite


class ClientSiteAdmin(admin.ModelAdmin):
    list_display = ('name', 'domain',)


admin.site.register(ClientSite, ClientSiteAdmin)
