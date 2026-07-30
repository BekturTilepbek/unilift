from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin
from unfold.admin import ModelAdmin

from .models import SiteSettings


@admin.register(SiteSettings)
class SiteSettingsAdmin(TabbedTranslationAdmin, ModelAdmin):
    fieldsets = (
        ("Контакты", {
            "fields": ("phone", "phone_display", "email"),
        }),
        ("Мессенджеры", {
            "fields": ("whatsapp", "telegram"),
        }),
        ("Адрес и часы работы", {
            "fields": ("address", "work_hours", "map_url"),
        }),
    )

    def has_add_permission(self, request):
        # Разрешаем создать запись только если её ещё нет вообще
        return not SiteSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False