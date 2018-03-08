from django.db import models

from headbutt.framework.core.models import Entity
from headbutt.framework.settings import HEADBUTT_FRAMEWORK_SETTINGS as SETTINGS


class AbstractExternalAuthentication(Entity):
    external_id = models.CharField(max_length=255)
    provider = models.IntegerField(choices=SETTINGS['AUTHENTICATION_PROVIDERS'])

    class Meta:
        abstract = True
        unique_together = ('external_id', 'provider')
