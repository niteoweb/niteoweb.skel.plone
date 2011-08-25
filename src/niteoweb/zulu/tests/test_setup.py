# -*- coding: utf-8 -*-
"""Setup/installation tests for this package."""

from niteoweb.zulu.tests.base import IntegrationTestCase
from Products.CMFCore.utils import getToolByName

import unittest2 as unittest


class TestCase(IntegrationTestCase):
    """Test installation of niteoweb.zulu into Plone."""

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.quickinstaller = getToolByName(self.portal, 'portal_quickinstaller')

    def test_product_installed(self):
        """Test if niteoweb.zulu is installed with portal_quickinstaller."""
        self.failUnless(self.installer.isProductInstalled('niteoweb.zulu'))

    def test_uninstall(self):
        """Test if niteoweb.zulu is cleanly uninstalled."""
        self.installer.uninstallProducts(['niteoweb.zulu'])
        self.failIf(self.installer.isProductInstalled('niteoweb.zulu'))

    # properties.xml
    def test_portal_title(self):
        """Test if portal title was correctly updated."""
        title = self.portal.getProperty('title')
        self.assertTrue(title.startswith("Zavod mladi podjetnik -"))

    # browserlayer.xml
    def test_browserlayer(self):
        """Test that INiteowebZuluLayer is registered."""
        from niteoweb.zulu.interfaces import INiteowebZuluLayer
        from plone.browserlayer import utils
        self.failUnless(INiteowebZuluLayer in utils.registered_layers())


def test_suite():
    """This sets up a test suite that actually runs the tests in the class
    above."""
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
