#!/usr/bin/env python
""" create a new django project using my custom templates """

from django_skeleton.management import start_project
import sys

if __name__ == '__main__':

    project_name = sys.argv[1]
    start_project(project_name)
