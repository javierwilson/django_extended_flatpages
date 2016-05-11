# -*- coding: utf-8 -*-

from django import forms
from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.admin import FlatpageForm
from django.contrib.flatpages.models import FlatPage
from django.utils.translation import ugettext_lazy as _
from django.forms.models import model_to_dict

from ckeditor.widgets import CKEditorWidget

from .models import CMSFlatPage


class CustomFlatpageForm(FlatpageForm):
    content = forms.CharField(widget=CKEditorWidget())
    description = forms.CharField(required=False, widget=forms.Textarea, label=_(u'Description'))
    keywords = forms.CharField(required=False, widget=forms.Textarea, label=_(u'Keywords'))

    def __init__(self, *args, **kwargs):
        _instance = kwargs.get("instance", None)
        if _instance:
            try:
                f = tuple(x.name for x in FlatPage._meta.fields)
                kwargs["initial"] = model_to_dict(_instance.cmsflatpage, f)
                kwargs["initial"].update(dict(
                    keywords=_instance.cmsflatpage.keywords,
                    description=_instance.cmsflatpage.description,
                ))
            except Exception as e:
                print e
        super(CustomFlatpageForm, self).__init__(*args, **kwargs)


class CustomFlatPageAdmin(FlatPageAdmin):
    form = CustomFlatpageForm
    fieldsets = (
        (None, {'fields': ('url', 'title', 'content', 'sites', 'keywords', 'description')}),
        (_('Advanced options'), {'classes': ('collapse',), 'fields': ('enable_comments', 'registration_required', 'template_name')}),
    )

    def save_model(self, request, obj, form, change):
        obj.save()
        page = dict(
            description=form.cleaned_data["description"],
            keywords=form.cleaned_data["keywords"],
        )
        print page
        cmsflatpage, b = CMSFlatPage.objects.get_or_create(page=obj, defaults=page)
        if not b:
            cmsflatpage.description = form.cleaned_data["description"]
            cmsflatpage.keywords = form.cleaned_data["keywords"]
        cmsflatpage.save()

admin.site.unregister(FlatPage)
admin.site.register(CMSFlatPage, CustomFlatPageAdmin)
