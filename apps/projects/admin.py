from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from modeltranslation.admin import TabbedTranslationAdmin
from unfold.admin import ModelAdmin, TabularInline

from .models import Project, ProjectCategory, ProjectImage


@admin.register(ProjectCategory)
class ProjectCategoryAdmin(TabbedTranslationAdmin, ModelAdmin):
    list_display = ("name", "slug", "order")
    list_editable = ("order",)
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name",)


class ProjectImageInline(TabularInline):
    model = ProjectImage
    extra = 1
    fields = ("image", "caption", "order")
    verbose_name = _("Фото")
    verbose_name_plural = _("Фотографии проекта")


@admin.register(Project)
class ProjectAdmin(TabbedTranslationAdmin, ModelAdmin):
    list_display = ("title", "city", "year", "is_published", "is_featured", "order")
    list_editable = ("is_published", "is_featured", "order")
    list_filter = ("is_published", "is_featured", "categories", "city")
    search_fields = ("title", "summary", "city", "client_name")
    prepopulated_fields = {"slug": ("title",)}
    filter_horizontal = ("categories",)
    inlines = [ProjectImageInline]

    fieldsets = (
        (_("Основное"), {
            "fields": ("title", "slug", "categories", "summary", "cover"),
        }),
        (_("Подробности"), {
            "fields": ("description", "city", "year", "client_name", "equipment"),
        }),
        (_("Публикация"), {
            "fields": ("is_published", "is_featured", "order"),
        }),
    )