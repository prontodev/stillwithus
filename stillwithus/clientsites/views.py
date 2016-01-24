import socket

from django.shortcuts import render
from django.views.generic import TemplateView

from .models import ClientSite
from servers.models import Server


class ClientSiteView(TemplateView):
    template_name = 'clientsites.html'

    def get(self, request):
        clientsites = ClientSite.objects.all()
        servers = Server.objects.all()

        results = []
        pronto_ips = [each.ip for each in servers]

        for each in clientsites:
            ip_list = []
            ais = socket.getaddrinfo(each.domain, 80, 0, 0, 0)
            for result in ais:
                ip_list.append(result[-1][0])
            ip_list = list(set(ip_list))
            for each_ip in ip_list:
                if each_ip in pronto_ips:
                    results.append((each.domain, 'Yes'))
            else:
                results.append((each.domain, 'No'))

        return render(
            request,
            self.template_name,
            {
                'results': results,
                'servers': servers
            }
        )
