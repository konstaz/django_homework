from django.contrib import admin  # noqa
from django.urls import path  # noqa

from students import views  # noqa
from group import views as g_views  # noqa
from teachers import views as t_views  # noqa

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello-world/', views.hello_world),
    path('students/', views.students),
    path('generate-student/', views.generate_student),
    path('generate-students/', views.generate_students),
    path('show-groups/', g_views.show_groups),
    path('show-teachers/', t_views.show_teachers)
]
