from datetime import date

from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Article

User = get_user_model()

class AuthorField(serializers.RelatedField):
    def to_representation(self, user):
        return user.get_full_name()

class ArticleSerializer(serializers.ModelSerializer):

    author = serializers.SlugRelatedField(queryset = User.objects.all(), slug_field=User.USERNAME_FIELD, many=True)
    links = serializers.SerializerMethodField()
    # author = serializers.SerializerMethodField()
    # author = AuthorField(many=True, queryset=User.objects.all())

    class Meta:
        model = Article
        fields = (
            'name',
            'content',
            'image',
            'category',
            'draft',
            'publish_date',
            'author',
            'links'
        )

    def get_links(self, obj):
        request = self.context['request']
        if obj:
            return {
                "self": reverse("article-detail", kwargs={"pk": obj.pk}, request=request),
            }

    def validate_publish_date(self, value):
        if value < date.today():
            msg = _("Publish date cannot be in the past.")
            raise serializers.ValidationError(msg)
        return attrs
