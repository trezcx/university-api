from rest_framework import routers
from uni.views import UserViewSet, UniversityViewSet

router = routers.DefaultRouter()

router.register(r'university', UniversityViewSet)
router.register(r'user', UserViewSet)

urlpatterns = [
    *router.urls
]