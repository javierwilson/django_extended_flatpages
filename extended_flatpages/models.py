from django.contrib.flatpages.models import FlatPage
from django.db import models
from django.utils.translation import ugettext_lazy as _


class CMSFlatPage(FlatPage):
    description = models.CharField(verbose_name=_(u"Description"), max_length=350)
    keywords = models.CharField(verbose_name=_(u"Keywords"), max_length=200)
    page = models.OneToOneField(FlatPage, verbose_name=_(u'Page'))
    image = models.ImageField(verbose_name=_(u'Image'), null=True, blank=True, upload_to='pages')

    class Meta:
        verbose_name = 'CMS Flat Pages'
