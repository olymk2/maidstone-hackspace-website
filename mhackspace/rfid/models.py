# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

# just brainstorming so we can start playing with this,
# be nice to make this a 3rd party django installable app ?


# users rfid card to user mapping, user can have more than one card
class Rfid(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True, blank=True,
        default=None,
        related_name='user'
    )
    code = models.PositiveIntegerField()
    description = models.CharField(_('Short rfid description', blank=True, max_length=255))

    def __str__(self):
        return self.description


# description of a device like door, print, laser cutter
class Devices(models.model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='+')
    name = models.CharField(_('Device name'), max_length=255)

    def __str__(self):
        return self.name


# device to user mapping, to check that the user is authorised
class RfidDevices(models.model):
    device = models.ForeignKey(
        Devices,
        null=True, blank=True,
        default=None,
        related_name='device'
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True, blank=True,
        default=None,
        related_name='user'
    )

