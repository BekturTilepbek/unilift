def site_settings(request):
    """
    Отдаёт общие для всех страниц данные (контакты, соцсети, часы работы) в шаблоны
    как `site`. Пока модель SiteSettings не подключена (Фаза 5), возвращает заглушки —
    шаблоны base.html/footer уже можно верстать против site.phone, site.address и т.д.
    """
    return {
        "site": {
            "phone": None,
            "phone_display": None,
            "whatsapp": None,
            "telegram": None,
            "email": None,
            "address": None,
            "work_hours": "Пн–Сб 09:00–18:00",
            "map_url": None,
        }
    }