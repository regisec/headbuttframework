# -*- coding: UTF-8 -*-

from django.conf import settings

HEADBUTT_FRAMEWORK_SETTINGS = getattr(settings, "HEADBUTT_FRAMEWORK_SETTINGS", {})

HEADBUTT_FRAMEWORK_SETTINGS.setdefault("APPS_FOLDER", settings.BASE_DIR)
