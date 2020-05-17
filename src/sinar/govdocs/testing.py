# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import sinar.govdocs


class SinarGovdocsLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=sinar.govdocs)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'sinar.govdocs:default')


SINAR_GOVDOCS_FIXTURE = SinarGovdocsLayer()


SINAR_GOVDOCS_INTEGRATION_TESTING = IntegrationTesting(
    bases=(SINAR_GOVDOCS_FIXTURE,),
    name='SinarGovdocsLayer:IntegrationTesting',
)


SINAR_GOVDOCS_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(SINAR_GOVDOCS_FIXTURE,),
    name='SinarGovdocsLayer:FunctionalTesting',
)


SINAR_GOVDOCS_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        SINAR_GOVDOCS_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='SinarGovdocsLayer:AcceptanceTesting',
)
