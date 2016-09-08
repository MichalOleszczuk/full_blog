from django.conf.urls import url, include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter(schema_title='Pastebin API')
router.register(r'posts', views.PostsViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'comments', views.CommentViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
]