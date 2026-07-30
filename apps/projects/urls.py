from django.urls import path

app_name = "projects"

# Каталог (list.html с фильтром по категориям + пагинацией) и детальные страницы
# (<slug>/ с галереей) добавляются в Фазе 3. Пока — пустой urlpatterns, чтобы
# include("apps.projects.urls") в config/urls.py не падал.
urlpatterns: list = []