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
    def test_server_admin_page_should_be_accessibale(self):
        admin = User.objects.create_superuser(
            'admin',
            'admin@test.com',
            'password'
        )
        self.client.login(
            username='admin',
            password='password'
        )
        url = '/admin/servers/server/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
