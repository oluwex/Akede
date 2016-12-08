from rest_framework.routers import DefaultRouter

from . import viewsets

router = DefaultRouter()
router.register(r'articles', viewsets.ArticleViewSet)