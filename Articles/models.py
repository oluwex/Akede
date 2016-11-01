from __future__ import unicode_literals

from django.db import models

# Create your models here.

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
    article = models.TextField(
        _('Oro Iroyin'),
        max_length=1000,
        help_text='Type the content of your article here'
    )
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    updated_time = models.DateTimeField(auto_now=True, auto_now_add=False)

    author = models.ManyToManyField(User, 'written_by')

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