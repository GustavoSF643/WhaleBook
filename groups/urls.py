from .views import GroupModelView
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(prefix=r'group', viewset=GroupModelView)

urlpatterns = router.urls

print(router.urls)
