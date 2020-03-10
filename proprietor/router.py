from .views import PersonApiView
from rest_framework import routers


router = routers.DefaultRouter()
router.register('proprietor', PersonApiView)