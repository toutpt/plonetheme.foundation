from setuptools import setup, find_packages

version = '1.0'

setup(name='plonetheme.foundation',
      version=version,
      description="",
      long_description=open("README.rst").read() + "\n" +
                       open("CHANGES.txt").read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Environment :: Web Environment",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
        "Framework :: Zope2",
        "Framework :: Plone",
        "Framework :: Plone :: 4.0",
        "Framework :: Plone :: 4.1",
        "Framework :: Plone :: 4.2",
        "Framework :: Plone :: 4.3",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
      ],
      keywords='plone',
      author='JeanMichel aka toutpt',
      author_email='toutpt@gmail.com',
      url='https://github.com/toutpt/plonetheme.foundation',
      license='gpl',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['plonetheme'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'plone.app.modernizr',
          'plone.app.theming',
          'plone.app.themingplugins',
          'plone.app.z3cform',
          'collective.js.ckeditor',
          'collective.js.enquire',
          'collective.js.foundation',
          'collective.z3cform.html5widgets',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
