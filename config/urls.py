from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.http import HttpResponse
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path

from apps.core.sitemaps import ProjectSitemap, StaticViewSitemap
from apps.core.views import robots_txt


def healthz(request):
    """Простой health-check для Docker/Caddy — без обращения к БД."""
    return HttpResponse("ok")


sitemaps = {
    "static": StaticViewSitemap,
    "projects": ProjectSitemap,
}

urlpatterns = [
    path("healthz/", healthz),
    path("i18n/", include("django.conf.urls.i18n")),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="sitemap"),
    path("robots.txt", robots_txt),
]

# prefix_default_language=False → русский остаётся на "/", кыргызский уезжает на "/ky/"
urlpatterns += i18n_patterns(
    path("admin/", admin.site.urls),
    path("projects/", include("apps.projects.urls")),
    path("", include("apps.core.urls")),
    prefix_default_language=False,
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    try:
        import debug_toolbar

        urlpatterns += [path("__debug__/", include(debug_toolbar.urls))]
    except ImportError:
        pass