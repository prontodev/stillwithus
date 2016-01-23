from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
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


class ClientSiteViewTest(TestCase):
    def test_clientsite_should_be_accessible(self):
        url = reverse('clientsites')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_clientsite_should_use_correct_template(self):
        url = reverse('clientsites')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'clientsites.html')


class ClientSiteAdminTest(TestCase):
    def test_clientsite_admin_page_should_be_accessible(self):
        admin = User.objects.create_superuser(
            'admin',
            'admin@test.com',
            'password'
        )
        self.client.login(
            username='admin',
            password='password'
        )
        url = '/admin/clientsites/clientsite/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
