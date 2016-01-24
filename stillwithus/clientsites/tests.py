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
    def setUp(self):
        self.url = reverse('clientsites')

    def test_clientsite_should_be_accessible(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_clientsite_should_use_correct_template(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'clientsites.html')

    def test_clientsite_should_render_html_correctly(self):
        response = self.client.get(self.url)

        expected = '<title>Still with Us?</title>'
        self.assertContains(response, expected, status_code=200)

        expected = '<h1>Client Sites</h1>'
        self.assertContains(response, expected, status_code=200)

        expected = '<table border="1">'
        self.assertContains(response, expected, status_code=200)

        expected = '<thead><tr><th>Domain</th><th>Still with Us?'
        expected += '</th></tr></thead>'
        self.assertContains(response, expected, status_code=200)

        expected = '<tr><td>www.prontomarketing.com</td><td>Yes</td></tr>'
        self.assertContains(response, expected, status_code=200)


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
