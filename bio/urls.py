from django.urls import path, include

from rest_framework.routers import DefaultRouter
from bio import views

router = DefaultRouter()
router.register('mybio', views.MyBioApiViewSet)

urlpatterns = [ 
    path('', include(router.urls))
]
