from datetime import date

from django.core.urlresolvers import reverse as reverse_web
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers
from rest_framework.reverse import reverse
from Articles.models import Article

User = get_user_model()

class AuthorField(serializers.RelatedField):
    def to_representation(self, user):
        return user.get_full_name()

class ArticleSerializer(serializers.ModelSerializer):

    category = serializers.SerializerMethodField()
    author = serializers.ReadOnlyField(source="author.get_full_name")
    links = serializers.SerializerMethodField()


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

    def get_category(self, obj):
        return obj.get_category_display()

    def get_links(self, obj):
        request = self.context['request']
        return {
            "self": reverse("article-detail", kwargs={"pk":obj.pk}, request=request),
            # "web_link": reverse_web("articles:detail", args=[obj.slug]),
        }

    def validate_publish_date(self, value):
        if value < date.today():
            msg = _("Publish date cannot be in the past.")
            raise serializers.ValidationError(msg)
        return value


# class ArticleSerializer(serializers.ModelSerializer):

#     author = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field=User.USERNAME_FIELD, many=True)

#     class Meta:
#         model = Article
#         fields = (
#             'url',
#             'name',
#             'content',
#             'image',
#             'category',
#             'draft',
#             'publish_date',
#             'author',
#             # 'links'
#         )

#     # def get_links(self, obj):
#     #     request = self.context["request"]
#     #     return {
#     #         "self": serializers.HyperlinkedIdentityField(
#     #             view_name="article",
#     #             lookup_field = "slug"
#     #         )
#     #     }

