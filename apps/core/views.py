from django.views.generic import TemplateView

from apps.projects.models import Project


class HomeView(TemplateView):
    template_name = "pages/home.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["featured_projects"] = (
            Project.objects.filter(is_published=True, is_featured=True)
            .prefetch_related("categories")
            .order_by("order", "-created_at")[:6]
        )
        return ctx