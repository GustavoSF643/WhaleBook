from .views import GroupModelView
from rest_framework.routers import SimpleRouter

router = SimpleRouter()

router.register(r'groups', GroupModelView, basename='groups')

urlpatterns = router.urls

