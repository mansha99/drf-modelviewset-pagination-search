from rest_framework import routers
from notices import views as noticeAppViews
router = routers.DefaultRouter()
router.register(r'notices', noticeAppViews.NoticeModelViewSet)
