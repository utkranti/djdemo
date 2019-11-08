from .views import StudViewset
from rest_framework import routers
from django.urls import path, include

router = routers.SimpleRouter()
router.register(r'twoapp', StudViewset)
# urlpatterns = [
#     path('', include(router.urls))
# ]
urlpatterns = router.urls