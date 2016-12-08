from __future__ import unicode_literals

# Create your models here.
from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.utils.text import slugify

# Create your models here.

class Article(models.Model):

    CATEGORIES = [
        ('Oselu', _('Oselu')),
        ('Gbogbogbo', _('Gbogbogbo')),
        ('Owo', _('Owo')),
    ]

    name = models.CharField(
        _('Akole Iroyin'),
        max_length=60,
        help_text='Name of the article',
        blank=False,
        null=False,
        unique=True,
    )
    content = models.TextField(
        _('Oro Iroyin'),
        max_length=1000,
        blank=False,
        null=True,
        help_text='Type the content of your article here'
    )

    slug = models.SlugField(unique=True)

    # TODO: 
    image = models.ImageField(null=True, blank=True, height_field="height_field", width_field="width_field")

    height_field = models.IntegerField(default=0)

    width_field = models.IntegerField(default=0)

    draft = models.BooleanField(default=False)

    publish_date = models.DateField(auto_now=False, auto_now_add=False)

    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name='Date published')

    updated = models.DateTimeField(auto_now=True, auto_now_add=False, verbose_name='Date updated')

    author = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='written_by', verbose_name="Author(s)")

    category = models.CharField(
        _("Ipele"),
        max_length=30,
        choices=CATEGORIES,
        blank=False,
        null=False,
    )

    class Meta:
        verbose_name = 'Iroyin'
        verbose_name_plural = 'Iroyin'


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('articles:detail', kwargs={'slug': self.slug})


def create_slug(instance, new_slug=None):
    slug = slugify(instance.name)
    if new_slug is not None:
        slug = new_slug
    qs = Article.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_article_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)


pre_save.connect(pre_save_article_receiver, sender=Article)