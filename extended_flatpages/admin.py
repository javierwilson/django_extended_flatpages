# -*- coding: utf-8 -*-

from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.admin import FlatpageForm
from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import CMSFlatPage


class CustomFlatpageForm(FlatpageForm):
    description = forms.CharField(required=False, widget=forms.Textarea, label=_(u'Description'))
    keywords = forms.CharField(required=False, widget=forms.Textarea, label=_(u'Keywords'))

    def save(self, commit=True):
        obj = super(CustomFlatpageForm, self).save(commit)
        obj.save()
        page = dict(
            description=self.cleaned_data["description"],
            keywords=self.cleaned_data["keywords"],
        )
        cmsflatpage = CMSFlatPage.objects.get_or_create(page=obj, defaults=page)
        cmsflatpage.save()


class CustomFlatPageAdmin(FlatPageAdmin): 
    form = CustomFlatpageForm
    fieldsets = (
        (None, {'fields': ('url', 'title', 'content', 'sites', 'keywords', 'description')}),
        (_('Advanced options'), {'classes': ('collapse',), 'fields': ('enable_comments', 'registration_required', 'template_name')}),
    )
