from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^create/$', Book.create.as_view(), name="create"),
]