from rest_framework import routers
from .views import VDayViewSet,VDayAnnotateViewSet

router = routers.DefaultRouter()
router.register(r'vdays', VDayViewSet)
router.register(r'vdays_annotate',VDayAnnotateViewSet)
