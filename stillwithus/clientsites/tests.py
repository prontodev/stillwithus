from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase

from .models import ClientSite
from servers.models import Server


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

    def test_clientsite_should_have_title(self):
        response = self.client.get(self.url)

        expected = '<title>Still with Us?</title>'
        self.assertContains(response, expected, status_code=200)

    def test_clientsite_should_render_html_for_clientsites_correctly(self):
        response = self.client.get(self.url)

        expected = '<h1>Client Sites</h1>'
        self.assertContains(response, expected, status_code=200)

        expected = '<thead><tr><th>Domain</th><th>Still with Us?'
        expected += '</th><th>Note</th></tr></thead>'
        self.assertContains(response, expected, status_code=200)

    def test_clientsite_should_query_domains_and_check_if_still_with_us(self):
        Server.objects.bulk_create([
            Server(name='Pronto 1', ip='54.72.3.133'),
            Server(name='Pronto 2', ip='54.72.3.103'),
            Server(name='Pronto 3', ip='54.252.146.70'),
            Server(name='Pronto 4', ip='54.67.50.151'),
            Server(name='Pronto 5', ip='52.1.32.33'),
            Server(name='Pronto 6', ip='27.254.65.18'),
            Server(name='Pronto 7', ip='54.246.93.4'),
            Server(name='Pronto 8', ip='54.228.219.35'),
            Server(name='Pronto 9', ip='54.72.3.253'),
            Server(name='Pronto 10', ip='54.171.171.172'),
            Server(name='Pronto 11', ip='46.137.96.191'),
            Server(name='Pronto 12', ip='54.194.28.91'),
            Server(name='Pronto 13', ip='54.72.53.55'),
        ])

        ClientSite.objects.create(
            name='Pronto',
            domain='www.prontomarketing.com'
        )
        ClientSite.objects.create(
            name='Atlas',
            domain='www.atlasperformancechicago.com'
        )

        response = self.client.get(self.url)

        expected = '<tr><td><a href="http://www.prontomarketing.com" '
        expected += 'target="_blank">www.prontomarketing.com</a></td>'
        expected += '<td style="color: red;">No</td><td></td></tr>'
        self.assertContains(response, expected, count=1, status_code=200)

        expected = '<td><a href="http://www.prontomarketing.com" '
        expected += 'target="_blank">www.prontomarketing.com</a></td>'
        self.assertContains(response, expected, count=1, status_code=200)

        expected = '<tr><td><a href="http://www.atlasperformancechicago.com" '
        expected += 'target="_blank">www.atlasperformancechicago.com</a></td>'
        expected += '<td>Yes</td><td></td></tr>'
        self.assertContains(response, expected, count=1, status_code=200)

        expected = '<td><a href="http://www.atlasperformancechicago.com" '
        expected += 'target="_blank">www.atlasperformancechicago.com</a></td>'
        self.assertContains(response, expected, count=1, status_code=200)

    def test_clientsite_should_render_html_for_servers_correctly(self):
        response = self.client.get(self.url)

        expected = '<h1>Servers</h1>'
        self.assertContains(response, expected, status_code=200)

        expected = '<thead><tr><th>Name</th><th>IP</th></tr></thead>'
        self.assertContains(response, expected, status_code=200)

    def test_clientsite_should_query_server_name_and_ip_correctly(self):
        Server.objects.create(
            name='AWS ELB',
            ip='54.72.3.133'
        )
        Server.objects.create(
            name='Bypronto',
            ip='54.171.171.172'
        )

        response = self.client.get(self.url)

        expected = '<tr><td>AWS ELB</td><td>54.72.3.133</td></tr>'
        self.assertContains(response, expected, status_code=200)

        expected = '<tr><td>Bypronto</td><td>54.171.171.172</td></tr>'
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
