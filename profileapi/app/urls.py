from django.urls import path,include
from .views import hello_world,HelloViewSet
from rest_framework.routers import DefaultRouter


router=DefaultRouter()
router.register('hello-viewset',HelloViewSet,basename='hello-viewset')


urlpatterns=[
    path('',hello_world.as_view()),
    path('',include(router.urls))
]
