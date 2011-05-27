from distutils.core import setup

setup(
  # basic package data
  name = "django-skeleton",
  version = "0.0.1",
  description = ''' my personal django settings ''',
  # package structure
  packages = ['skeleton',
              'skeleton.conf',
              'skeleton.conf.project_template',
              ],
  package_data = {'skeleton.conf.project_template': ['*.txt']},
  scripts =['skeleton/bin/django-createproject.py',],
)
