from django.views.generic import TemplateView


class HomeView(TemplateView):
    """
    Секции лендинга (hero, stats, партнёрство, оборудование, услуги, отрасли,
    о компании, проекты, контакты) собираются в Фазе 2. Сейчас шаблон
    подтверждает, что base.html, статика и шрифты подключены корректно.
    """

    template_name = "pages/home.html"