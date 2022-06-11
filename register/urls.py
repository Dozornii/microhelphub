from django.urls import re_path
from register import views as core_views

urlpatterns = [
    re_path(r'^register/$', core_views.register, name='register'),
]
