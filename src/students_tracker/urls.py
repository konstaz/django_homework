from django.contrib import admin  # noqa
from django.urls import include, path  # noqa
from django.conf import settings  # noqa
from django.conf.urls import url  # noqa

from students import views  # noqa

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('students/', include('students.urls')),
    path('teachers/', include('teachers.urls')),
    path('groups/', include('group.urls')),
    path('contact/', views.contact, name='contact'),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

urlpatterns += [url(r'^silk/', include('silk.urls', namespace='silk'))]
