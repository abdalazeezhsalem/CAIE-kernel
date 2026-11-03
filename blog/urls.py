from django.urls import path

from rest_framework.routers import DefaultRouter

from .views import PostViewSet , UserViewSet , CommentViewSet,CategoryViewSet #, get_posts

router = DefaultRouter()
router.register('api/posts', PostViewSet)
router.register('api/users', UserViewSet)
router.register('api/categories',CategoryViewSet )
router.register('api/comments',CommentViewSet)

urlpatterns = []
urlpatterns +=router.urls



# urlpatterns = [
#     path('posts/get_post/', get_posts, name='get_post'),
# ]