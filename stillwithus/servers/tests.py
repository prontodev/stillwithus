from django.contrib.auth.models import User
from django.test import TestCase

from .models import Server


class ServerTest(TestCase):
    def test_create_new_server(self):
        server = Server()
        server.name = 'Pronto World'
        server.ip = '54.71.191.111'

        self.assertFalse(server.id)
        server.save()
        self.assertTrue(server.id)

        server = Server.objects.get(id=server.id)
        self.assertEqual(server.name, 'Pronto World')
        self.assertEqual(server.ip, '54.71.191.111')


class ClientSiteAdminTest(TestCase):
    def setUp(self):
        admin = User.objects.create_superuser(
            'admin',
            'admin@test.com',
            'password'
        )
        self.client.login(
            username='admin',
            password='password'
        )
        self.url = '/admin/servers/server/'

    def test_server_admin_page_should_be_accessibale(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_server_admin_page_should_name_and_ip_columns(self):
        Server.objects.create(
            name='Bypronto',
            ip='54.171.171.100'
        )

        response = self.client.get(self.url)

        expected = '<div class="text"><a href="?o=1">Name</a></div>'
        self.assertContains(response, expected, status_code=200)

        expected = '<div class="text"><a href="?o=2">Ip</a></div>'
        self.assertContains(response, expected, status_code=200)
