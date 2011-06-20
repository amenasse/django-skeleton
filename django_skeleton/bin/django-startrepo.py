#!/usr/bin/env python 

import sys
from optparse import OptionParser

def main(args):

    parser = OptionParser(usage="\n\tcreate a new django based project repository\n\n%prog [options] [REPO NAME]..",version="%prog %(VERSION)")

    parser.add_option("-p","--project",
                      dest="project_name",default=None,
                      help="name for django project to use in the repository. Defaults to REPO_NAME")


    (options, args) = parser.parse_args()

    from django_skeleton.fabfile import django_repo_init
    from django_skeleton.fabfile import setup_virtualenv

    repo_name = args[0]
    project_name = options.project_name or repo_name
    django_repo_init(repo_name,project_name)
    setup_virtualenv(project_name)


if __name__ == '__main__':
    main(sys.argv)



