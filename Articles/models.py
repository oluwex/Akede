from __future__ import unicode_literals

# Create your models here.
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

# Create your models here.

class Article(models.Model):

    CATEGORIES = [
        ('politics', _('Oselu')),
        ('general', _('Gbogbogbo'))
    ]

    name = models.CharField(
        _('Akole Iroyin'),
        max_length=60,
        help_text='Name of the article',
        blank=False,
        null=False,
    )
    content = models.TextField(
        _('Oro Iroyin'),
        max_length=1000,
        help_text='Type the content of your article here'
    )

    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name='Date published')

    updated = models.DateTimeField(auto_now=True, auto_now_add=False, verbose_name='Date updated')

    author = models.ManyToManyField(User, related_name='written_by', verbose_name="Author(s)")

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


    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('articles:detail', kwargs={'id': self.id})