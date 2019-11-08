from .views import EmpViewset
from rest_framework import routers
from django.urls import path, include

router = routers.SimpleRouter()
router.register(r'oneapp', EmpViewset)

# urlpatterns = [
#     path('', include(router.urls))
# ]

urlpatterns = router.urls