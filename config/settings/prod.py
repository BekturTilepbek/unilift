import os

from .base import *  # noqa: F403

DEBUG = False

if not ALLOWED_HOSTS:  # noqa: F405
    raise ValueError(
        "DJANGO_ALLOWED_HOSTS обязателен в проде — укажите домен(ы) через запятую в .env"
    )

# Cloudflare терминирует TLS перед Caddy; Caddy отдаёт по HTTPS дальше.
# По умолчанию считаем, что HTTPS есть (обычный прод с доменом и Caddy).
# Для временного демо-деплоя по IP без домена — выставить
# DJANGO_SECURE_SSL_REDIRECT=False в .env, это отключит весь HTTPS-блок ниже.
HTTPS_ENABLED = os.environ.get("DJANGO_SECURE_SSL_REDIRECT", "True") == "True"

if HTTPS_ENABLED:
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = "SAMEORIGIN"

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = os.environ.get("EMAIL_HOST", "")
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER", "")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD", "")
EMAIL_PORT = int(os.environ.get("EMAIL_PORT", 587))
EMAIL_USE_TLS = True

SENTRY_DSN = os.environ.get("SENTRY_DSN", "")
if SENTRY_DSN:
    import sentry_sdk
    from sentry_sdk.integrations.django import DjangoIntegration

    sentry_sdk.init(
        dsn=SENTRY_DSN,
        integrations=[DjangoIntegration()],
        traces_sample_rate=0.1,
        send_default_pii=False,
    )