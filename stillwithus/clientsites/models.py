from __future__ import unicode_literals

from django.db import models


class ClientSite(models.Model):
    domain = models.CharField(
        null=True,
        blank=True,
        max_length=500
    )
