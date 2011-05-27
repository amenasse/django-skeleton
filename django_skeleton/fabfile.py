""" fabfile for bootstrapping new django projects """
from fabric.api import *
from fabric.contrib.project import rsync_project
import os

def create_django_project(project_name):
    """ create the initial repository containing a new django project """

    cwd = os.getcwd()
    local('git init %s' % project_name)
    repo_dir = os.path.join(cwd,project_name)

    with lcd(repo_dir):

        source_dir = os.path.join(repo_dir,'src')
        os.mkdir(source_dir)

    with lcd(source_dir):
        import django_skeleton.conf
        source_template = os.path.realpath(django_skeleton.conf.__path__[0])
        local('rsync -av --exclude project_template %s/ %s' % (source_template,source_dir))
        local('django-startproject.py %s' % project_name)
