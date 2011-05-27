#!/usr/bin/env python 

import sys

def main(args):

    from django_skeleton.fabfile import django_repo_init
    project_name = args[1]
    django_repo_init(project_name)


if __name__ == '__main__':
    main(sys.argv)



