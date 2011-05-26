#!/usr/bin/env python

"""
setup virtual environment
requires virtualenv and pip to be installed.

"""

import os
import subprocess
import shutil

current_path = os.path.realpath(__file__)

current_dir = os.path.dirname(current_path)
project_name = current_dir.split(os.sep)[-2]


subprocess.call(["pip","install",
                    "-E",project_name,
                    "--ignore-installed",
                    "--requirement",os.path.join(current_dir,"../requirements.txt")])
