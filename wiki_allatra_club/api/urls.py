from django.conf.urls import url, include
from rest_framework import routers
from . import views

from rest_framework import routers
router = routers.DefaultRouter()

router.register(r'annotation', views.AnnotationViewSet)

urlpatterns = [
    url(r'', include(router.urls)),
    url(r'search', views.search),
]