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

This theme is mobile first, it means all features are working on a mobile device
and are enhanced for desktop.

* http://en.wikipedia.org/wiki/Progressive_enhancement

HTML 5
------

Forms are all based on z3cform and widgets are all HTML5 base widgets using
the addon collective.z3cform.html5widgets

If you want to stay compatible with incapable browser you must consider to
add polyfills to your project. For example collective.js.webshims

Read about compatibilities:

* http://mobilehtml5.org/
* http://www.wufoo.com/html5/

TODO
----

We depends on jqueryui because of autocomplete. It's the time to implements
an ajax datalist widget in collective.z3cform.html5widgets
