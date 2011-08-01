===============
django-skeleton
===============

this is my personal django skeleton in order to provide a starting point for 
new django projects.

Its really just the standard django project layout as produced by 
``django-admin.py startproject`` with a few minor tweaks.

A requirements.txt file for use with virtualenv is also included. 

The following command line tools are implemented to bootstrap projects


``django-startproject.py`` : this is similar to the ``startproject`` 
django-admin command, except it used my custom project template


``django-startrepo.py`` : for the given project name this script will perform 
a series of steps to prepare the project for development.

Currently it does the following:
    * generates a git repository
    * creates a virtualenv
    * runs ``django-startproject``  to create the initial project layout
    * installs the default set of packages from ``requirements.txt``
