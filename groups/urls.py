from .views import GroupView, GroupGoalsView
from rest_framework.routers import SimpleRouter

router = SimpleRouter()

router.register(r'groups', GroupView, basename='groups')
router.register('groups/(?P<pk>[^/.]+)/goals', GroupGoalsView, basename='group_goals')


urlpatterns = router.urls



