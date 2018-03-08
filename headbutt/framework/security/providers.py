import random
from abc import abstractmethod
from django.core.cache import cache
from django.core.mail import send_mail
from headbutt.framework.settings import HEADBUTT_FRAMEWORK_SETTINGS as SETTINGS
from string import digits


class AbstractExternalAuthenticationProvider(object):

    @abstractmethod
    def send(self, external_id):
        raise NotImplementedError

    @abstractmethod
    def process(self, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def get_status(self, **kwargs):
        raise NotImplementedError


class EmailAuthenticationProvider(AbstractExternalAuthenticationProvider):
    def __init__(self, code_size=4, code_timeout=300):
        self._code_size = code_size
        self._code_timeout = code_timeout

    def send(self, external_id):
        code = ''.join([random.choice(digits) for _ in range(self._code_size)])
        cache.set('EMAIL_AUTH_FOR_' + external_id, code, self._code_timeout)
        # TODO
        send_mail('')

    def process(self, **kwargs):
        pass

    def get_status(self, **kwargs):
        pass