from django.conf.urls import url
from . import views
urlpatterns=[
    url(r'^places/',views.test,name='test'),
    url(r'^test/',views.place,name='place'),
]