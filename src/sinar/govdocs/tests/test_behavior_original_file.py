# -*- coding: utf-8 -*-
from sinar.govdocs.behaviors.original_file import IOriginalFileMarker
from sinar.govdocs.testing import SINAR_GOVDOCS_INTEGRATION_TESTING  # noqa
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.behavior.interfaces import IBehavior
from zope.component import getUtility

import unittest


class OriginalFileIntegrationTest(unittest.TestCase):

    layer = SINAR_GOVDOCS_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_behavior_original_file(self):
        behavior = getUtility(IBehavior, 'sinar.govdocs.original_file')
        self.assertEqual(
            behavior.marker,
            IOriginalFileMarker,
        )
