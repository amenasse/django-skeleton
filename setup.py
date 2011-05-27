from distutils.core import setup
import os

# following functions taken from
# http://wiki.python.org/moin/Distutils/Cookbook/AutoPackageDiscovery

def is_package(path):
    return (
        os.path.isdir(path) and
        os.path.isfile(os.path.join(path, '__init__.py'))
        )



def find_packages(path, base="" ):
    """ Find all packages in path """
    packages = {}
    for item in os.listdir(path):
        dir = os.path.join(path, item)
        if is_package( dir ):
            if base:
                module_name = "%(base)s.%(item)s" % vars()
            else:
                module_name = item
            packages[module_name] = dir
            packages.update(find_packages(dir, module_name))
    return packages

packages = find_packages('.')

setup(
  # basic package data
  name = "django-skeleton",
  version = "0.0.1",
  description = ''' my personal django settings ''',
  # package structure
  packages = packages.keys(),
  package_data = dict([(package,['*.txt']) for package in packages.keys() ]),

  scripts =['django_skeleton/bin/django-createproject.py',
            'django_skeleton/bin/django-repoinit.py',
  ],
)
