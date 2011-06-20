""" fabfile for bootstrapping new django projects """
from fabric.api import *
from fabric.contrib.project import rsync_project
import os

def django_repo_init(repo_name,project_name=None):
    """ create the initial git repository in the current directory """

    cwd = os.getcwd()
    # create the git repo
    local('git init %s' % repo_name)
    repo_dir = os.path.join(cwd,repo_name)

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
    if project_name is None:
        project_name = repo_name

    old_dir = os.getcwd()
    os.chdir(dest)
    start_project(project_name)
    os.chdir(old_dir)

def setup_virtualenv(name):
    """ create a new virtualenv and install initial packages """

    virtualenv_wrapper = local("which virtualenvwrapper.sh",capture=True)
    local("source %s  && mkvirtualenv --no-site-packages %s" % (virtualenv_wrapper,name))

    cwd = os.getcwd()
    project_dir = os.path.join(cwd,name)
    requirements_file = os.path.join(project_dir,'src','requirements.txt')

    virtualenv_path = os.path.join(os.environ['WORKON_HOME'],name)

    with lcd(project_dir):
        local('pip install -r %s -E %s' % (requirements_file,virtualenv_path))
