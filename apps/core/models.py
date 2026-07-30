from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _


class SiteSettings(models.Model):
    """
    Синглтон — в базе всегда ровно одна запись. Редактируется из админки клиентом,
    без участия разработчика. Заполняется реальными контактами в этой фазе —
    до тех пор все поля стоят как плейсхолдеры.
    """

    phone = models.CharField(
        _("Телефон (для ссылки tel:)"), max_length=20, blank=True,
        help_text=_("В международном формате, например: +996700123456"),
    )
    phone_display = models.CharField(
        _("Телефон (для отображения)"), max_length=30, blank=True,
        help_text=_("Как показывать на сайте, например: +996 700 123 456"),
    )
    whatsapp = models.URLField(_("Ссылка WhatsApp"), blank=True, help_text=_("Например: https://wa.me/996700123456"))
    telegram = models.URLField(_("Ссылка Telegram"), blank=True, help_text=_("Например: https://t.me/unilift"))
    email = models.EmailField(_("Email"), blank=True)

    address = models.CharField(_("Адрес"), max_length=300, blank=True)
    work_hours = models.CharField(_("Часы работы"), max_length=200, blank=True, default="Пн–Сб 09:00–18:00")
    map_url = models.URLField(_("Ссылка на карту"), blank=True, help_text=_("Ссылка на 2ГИС/Google Maps для кнопки «Как проехать»"))

    class Meta:
        verbose_name = _("Настройки сайта")
        verbose_name_plural = _("Настройки сайта")

    def __str__(self):
        return "Настройки сайта"

    def save(self, *args, **kwargs):
        self.pk = 1  # синглтон: всегда одна и та же запись
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass  # запрещаем удаление — на сайте всегда должна быть хотя бы одна запись

    @classmethod
    def load(cls):
        obj, _created = cls.objects.get_or_create(pk=1)
        return obj