from posts.viewsets import PostModelViewset, PostViewset
from rest_framework.routers import DefaultRouter



router = DefaultRouter()

router.register("posts", PostViewset, basename="posts")

# router.register("posts", PostModelViewset, basename="posts")

urlpatterns = router.urls
