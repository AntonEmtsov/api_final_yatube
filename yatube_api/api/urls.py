from django.urls import include, path
from rest_framework import routers

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet


router_v_1_0 = routers.DefaultRouter()
router_v_1_0.register('posts', PostViewSet, basename='posts')
router_v_1_0.register('groups', GroupViewSet, basename='groups')
router_v_1_0.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)
router_v_1_0.register('follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('v1/', include(router_v_1_0.urls)),
    path('v1/', include('djoser.urls.jwt')),
]
