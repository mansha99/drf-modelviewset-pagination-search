from rest_framework.routers import DefaultRouter,SimpleRouter
router = DefaultRouter()
from django.urls.conf import  path,include
from .views import NoticeModelViewSet
# register viewset with router
router.register("NoticeApi", NoticeModelViewSet, basename="Notice")
urlpatterns = [
    path('', include(router.urls))
]