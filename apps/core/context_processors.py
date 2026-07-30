from .models import SiteSettings


def site_settings(request):
    """
    Отдаёт контакты клиента во все шаблоны как `site`. Данные читаются из
    единственной записи SiteSettings — редактируется в админке без участия
    разработчика.
    """
    settings_obj = SiteSettings.load()
    return {
        "site": {
            "phone": settings_obj.phone,
            "phone_display": settings_obj.phone_display,
            "whatsapp": settings_obj.whatsapp,
            "telegram": settings_obj.telegram,
            "email": settings_obj.email,
            "address": settings_obj.address,
            "work_hours": settings_obj.work_hours,
            "map_url": settings_obj.map_url,
        }
    }