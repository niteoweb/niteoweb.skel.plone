# -*- coding: utf-8 -*-
"""Installer for this package."""

from setuptools import setup, find_packages

# shamlessly stolen from Hexagon IT guys :)
def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

version = read('niteoweb', 'zulu', 'version.txt').strip()

setup(name='niteoweb.zulu',
      version=version,
      description="A portal for young entrepreneurs in Slovenia.",
      long_description=
        read('README.rst') +
        read('HISTORY.rst') +
        read('LICENSE.rst') +
      ))
    
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='Plone Python',
      author='NiteoWeb Ltd.',
      author_email='info@niteoweb.com',
      url='',
      license='BSD',
      packages=find_packages('src', exclude=['ez_setup']),
      namespace_packages=['niteoweb'],
      package_dir={'': 'src'},
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # list project dependencies
          'niteoweb.loginas',
          'plone.app.caching',
          'plone.app.testing',
          'plone.app.theming',
          'setuptools',

      ],
      extras_require={
          # list libs needed for unittesting this project
          'test': [
              'mock',
              'plone.app.testing',
              'transmogrify.filesystem',
              'unittest2',
          ]
      },
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )