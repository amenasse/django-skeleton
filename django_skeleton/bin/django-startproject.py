#!/usr/bin/env python
""" create a new django project using my custom templates """

import sys

def main(args):

    from django_skeleton.management import start_project
    project_name = args[1]
    start_project(project_name)


if __name__ == '__main__':
    main(sys.argv)
