from django.conf import settings as django_settings

__all__ = ["settings"]


class LazySettings:
    HIJACK_PERMISSION_CHECK = "hijack.permissions.superusers_only"
    HIJACK_INSERT_BEFORE = "</body>"
    HIJACKED_AUTHENTICATION_BACKEND = ""
    HIJACKER_AUTHENTIACTION_BACKEND = ""

    def __getattribute__(self, name):
        try:
            return getattr(django_settings, name)
        except AttributeError:
            return super().__getattribute__(name)


settings = LazySettings()
