from django.contrib.auth import get_user_model
from django.http import Http404

from rest_framework import viewsets, authentication, permissions, filters
from rest_framework.response import Response
from rest_framework.decorators import detail_route

from .serializers import ArticleSerializer
from Articles.models import Article
from .permissions import IsOwnerOrReadOnly

class DefaultMixin(object):
    authentication_classes = (
        authentication.BasicAuthentication,
        authentication.TokenAuthentication,
    )
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly
    )
    paginate_by = 25
    paginate_by_param = 'page_size'
    max_paginate_by = 100
    filter_backends = (
        filters.DjangoFilterBackend,
        filters.SearchFilter,
    )


class ArticleViewSet(DefaultMixin, viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    search_fields = ('name', 'publish_date', 'category')

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    # @detail_route(methods=['get'], permission_classes=[IsOwnerOrReadOnly])
    # def get_absolute_url(self, request, slug=None):
    #     article = Article.objects.get(pk=slug)
    #     serializer = ArticleSerializer(article)
    #     return Response(serializer.data)


# class ArticleDetail(generics.RetrieveAPIView):

#     def get(self, request, *args, **kwargs):
#         slug = kwargs['slug']
#         article = Article.objects.get(slug=slug)
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data)