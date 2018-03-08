import uuid
from django.db import models


class Entity(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    disabled_at = models.DateTimeField(null=True, default=None)

    class Meta:
        abstract = True

    @property
    def is_enabled(self):
        return self.disabled_at is None

    @property
    def is_disabled(self):
        return not self.is_enabled
