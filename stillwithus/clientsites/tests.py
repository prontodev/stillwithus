from django.test import TestCase

from .models import ClientSite


class ClientSiteTest(TestCase):
    def test_create_new_clientsite(self):
        clientsite = ClientSite()
        clientsite.name = 'Atlas'
        clientsite.domain = 'www.atlasperformancechicago.com'

        self.assertFalse(clientsite.id)
        clientsite.save()
        self.assertTrue(clientsite.id)

        clientsite = ClientSite.objects.get(id=clientsite.id)
        self.assertEqual(clientsite.name, 'Atlas')
        self.assertEqual(clientsite.domain, 'www.atlasperformancechicago.com')
