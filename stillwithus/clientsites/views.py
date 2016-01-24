from django.shortcuts import render
from django.views.generic import TemplateView


class ClientSiteView(TemplateView):
    template_name = 'clientsites.html'

    def get(self, request):
        return render(
            request,
            self.template_name,
            {}
        )
