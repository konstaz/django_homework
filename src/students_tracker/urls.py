from django.contrib import admin
from django.urls import path

from students import views
from group import views as g_views
from teachers import views as t_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello-world/', views.hello_world),
    path('students/', views.students),
    path('generate-student/', views.generate_student),
    path('generate-students/', views.generate_students),
    path('show-groups/', g_views.show_groups),
    path('show-teachers/', t_views.show_teachers)
]
