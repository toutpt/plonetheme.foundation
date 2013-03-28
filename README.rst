Introduction
============

This addon is a base theme for the CMS Plone. It provides a different design
and code base for the UI.

Features
========

* mobile first
* dexterity support only (plone.app.contenttypes)
* html 5
* css 3
* based on foundation (by zurb)
* use stiky top navigation bar (ala twitter bootstrap)
* ckeditor 4 wysiwyg

Dexterity
---------

Dexterity is the next generation content type engine for the CMS Plone. The
Plone integration is done by plone.app.contenttypes.

Mobile first
------------

This theme is mobile first, it means all features are working on a mobile
device and are enhanced for desktop.

* http://en.wikipedia.org/wiki/Progressive_enhancement

To achieve this there is a plonetheme.foundationdesk theme inside this one
where resources are loaded by ajax and triggered by screen with (may change
in the future)

HTML 5
------

Forms are all based on z3cform and widgets are all HTML5 base widgets using
the addon collective.z3cform.html5widgets

If you want to stay compatible with incapable browser you must consider to
add polyfills to your project. For example collective.js.webshims

Read about compatibilities:

* http://mobilehtml5.org/
* http://www.wufoo.com/html5/

Layout has also been improved by using more semantic HTML tags where it's
possible.

This addon remove ...
---------------------

This add remove archetypes, so any addons using archetypes will be broken.

removed skins from portal_skins:

* referencebrowser
* tinymce
* archetypes
* archetypes_kss
* ATContentTypes
* plone_ecmascript
* plone_styles
* plone_images
* plone_3rdParty
* cmf_legacy


TODO
====

RelatedItems support ?
-----------------------

The widget at the moment is for desktop and need jqueryui + contenttree
as javascript depednencies.

Options we have:
* do not support related items for mobile and make a widget which is loaded by JS for desktop
* support it using a simple "ajax search" widget without dependencies

folder_contents
---------------

Table are not responsive friends. There are many way to display tables on
mobile but I would prefere not have table at all.

Ideas:
* treat folder_contents as a mailbox and create a more NUI for this one.
* use a responsive table approch (which one ?) with as few resources as possible

Upstream some of changes done in this addon
-------------------------------------------

edit bar and status messages are hard coded in many templates:

* main_template
* dashboard
* ...

theses has been done using viewlet so changing the HTML of theses becomes really easy.


