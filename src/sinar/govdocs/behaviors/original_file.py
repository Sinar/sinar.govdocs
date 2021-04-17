# -*- coding: utf-8 -*-

from sinar.govdocs import _
from plone import schema
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from Products.CMFPlone.utils import safe_hasattr
from zope.component import adapter
from zope.interface import Interface
from zope.interface import implementer
from zope.interface import provider
from plone.namedfile.field import NamedBlobFile




class IOriginalFileMarker(Interface):
    pass


@provider(IFormFieldProvider)
class IOriginalFile(model.Schema):
    """
    """

    original_file = NamedBlobFile(
        title=_(u'Original File'),
        description=_(u'Original scan or document'),
        required=False,
    )


@implementer(IOriginalFile)
@adapter(IOriginalFileMarker)
class OriginalFile(object):
    def __init__(self, context):
        self.context = context

    @property
    def original_file(self):
        if safe_hasattr(self.context, 'original_file'):
            return self.context.original_file
        return None

    @original_file.setter
    def original_file(self, value):
        self.context.original_file= value
