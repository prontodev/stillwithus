from django.shortcuts import render
from django.views.generic import TemplateView

from .models import ClientSite


class ClientSiteView(TemplateView):
    template_name = 'clientsites.html'

    def get(self, request):
        clientsites = ClientSite.objects.all()

        return render(
            request,
            self.template_name,
            {
                'clientsites': clientsites
            }
        )
