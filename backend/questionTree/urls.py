from rest_framework import routers
from .views import WebAppViewSet, RequirementViewSet, IndustryViewSet

router = routers.DefaultRouter()
router.register(r'webapps', WebAppViewSet, basename="webapps")
router.register(r'requirements', RequirementViewSet)
router.register(r'industries', IndustryViewSet)


urlpatterns = router.urls