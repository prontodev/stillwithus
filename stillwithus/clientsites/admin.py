from django.contrib import admin

from .models import ClientSite


class ClientSiteAdmin(admin.ModelAdmin):
    list_display = ('domain',)


admin.site.register(ClientSite, ClientSiteAdmin)
