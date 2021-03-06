from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        regex=r'^find/$',
        view=views.find.as_view(),
        name='find'
    ),
    url(
        regex=r'^set/$',
        view=views.set.as_view(),
        name='set'
    ),
]