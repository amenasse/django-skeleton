""" fabfile for bootstrapping new django projects """
from fabric.api import *
from fabric.contrib.project import rsync_project
import os

def django_repo_init(project_name):
    """ create the initial git repository in the current directory """

    cwd = os.getcwd()
    # create the git repo
    local('git init %s' % project_name)
    repo_dir = os.path.join(cwd,project_name)

    with lcd(repo_dir):
        source_dir = os.path.join(repo_dir,'src')
        os.mkdir(source_dir)

    dest = source_dir

    # sync everything but the project template first
    with lcd(dest):
        import django_skeleton.conf
        source_template = os.path.realpath(django_skeleton.conf.__path__[0])
        local('rsync -av --exclude project_template %s/ %s' % (source_template,dest))

    from django_skeleton.management import start_project
    os.chdir(dest)
    start_project(project_name)
