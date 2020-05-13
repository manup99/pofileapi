from django.urls import path,include
from .views import hello_world,HelloViewSet,ProfileViewSet,LoginViewSet
from rest_framework.routers import DefaultRouter


router=DefaultRouter()
router.register('hello-viewset',HelloViewSet,basename='hello-viewset')
router.register('profile-viewset',ProfileViewSet)

"""No need to assign base name as it will itself configure name through queryset provided"""

urlpatterns=[
    path('',hello_world.as_view()),
    path('login',LoginViewSet.as_view()),
    path('',include(router.urls))
]
