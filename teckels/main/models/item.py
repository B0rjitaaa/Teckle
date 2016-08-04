from hashlib import sha1
import os
from uuid import uuid4
from decimal import Decimal, ROUND_HALF_UP

from django.core.validators import MinValueValidator
from django.core.validators import RegexValidator

from django.template import defaultfilters

from django.db import models

from django.utils.translation import ugettext_lazy as _

def upload_to(instance, filename):
    ext = filename.split('.')[-1]
    # get filename
        # set filename as random string
    filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join('images/items', filename)


class Item(models.Model):
    official_name = models.CharField(
        _('Nombre oficial'),
        max_length=100,
        blank=True,
        null=True
    )
    familiar_name = models.CharField(
        _('Nombre familiar'),
        max_length=150,
        blank=True,
        null=True
    )
    father = models.CharField(
        _('Padre'),
        max_length=150,
        blank=True,
        null=True
    )
    mother = models.CharField(
        _('Madre'),
        max_length=150,
        blank=True,
        null=True
    )
    sex = models.CharField(
        _('Sexo'),
        max_length=10,
        blank=True,
        null=True
    )
    colour = models.CharField(
        _('Color'),
        max_length=150,
        blank=True,
        null=True
    )
    size = models.CharField(
        _('Tamaño'),
        max_length=150,
        blank=True,
        null=True
    )
    born_date = models.DateField(
        _('Fecha nacimiento'),
        blank=True,
        null=True
    )
    shown_times = models.PositiveIntegerField(
        _('shown times'),
        default=0
    )
    slug = models.SlugField(
        max_length=100,
        null=True,
        blank=True
    )
    category = models.ForeignKey(
        'Category',
        related_name='items',
        related_query_name='item',
        verbose_name=_('Pelo'),
        blank=True,
        null=True
    )
    comments = models.CharField(
        _('Comentarios'),
        max_length=500,
        blank=True,
        null=True
    )
    image = models.ImageField(
      upload_to=upload_to,
      null=True,
      blank=True,
      max_length=1000
    )
    second_image = models.ImageField(
      upload_to=upload_to,
      null=True,
      blank=True,
      max_length=1000
    )
    third_image = models.ImageField(
      upload_to=upload_to,
      null=True,
      blank=True,
      max_length=1000
    )
    fourth_image = models.ImageField(
      upload_to=upload_to,
      null=True,
      blank=True,
      max_length=1000
    )
    class Meta:
        verbose_name = "Teckel"
        verbose_name_plural = "Teckles"

    def __str__(self):
        if self.official_name:
            return self.official_name
        else:
            return self.familiar_name

    def save(self, *args, **kwargs):
        if self.official_name:
            self.slug = defaultfilters.slugify(self.official_name)
        else:
            self.slug = defaultfilters.slugify(self.familiar_name)
        super(Item, self).save(*args, **kwargs)