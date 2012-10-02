from setuptools import setup, find_packages
import os

version = '0.3.6.dev0'

setup(name='plonenl.plonetheme',
      version=version,
      description="Plone.nl Plone Theme",
      long_description=open("README.rst").read() + "\n" +
                       open("CHANGES.rst").read(),
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='web zope plone theme',
      author='Plone.nl',
      author_email='support@fourdigits.nl',
      url='http://plone.nl',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['plonenl'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'collective.ploneslimbar',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      setup_requires=["PasteScript"],
      paster_plugins = ["ZopeSkel"],
      )
