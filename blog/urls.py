from django.contrib import admin
from django.urls import path, include, re_path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.views.static import serve
from apps.posts import urls as posts_urls
from apps.tasks import urls as tasks_urls
from apps.perfil import urls as perfil_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(posts_urls)),
    path('', include(tasks_urls)),
    path('', include(perfil_urls)),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    })
]
