from Articles.APIArea import viewsets
from rest_framework.routers import DefaultRouter
from Articles.views import detail

router = DefaultRouter()
router.register(r'articles', viewsets.ArticleViewSet)