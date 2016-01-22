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
