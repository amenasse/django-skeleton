#!/usr/bin/env python

"""
setup virtual environment
requires virtualenv and pip to be installed.

"""

import os
import subprocess
import shutil


pwd = os.path.dirname(__file__)

vedir = os.path.join(pwd,"ve")

if os.path.exists(vedir):
    shutil.rmtree(vedir)

subprocess.call(["pip","install",
                    "-E",vedir,
                    "--ignore-installed",
                    "--requirement",os.path.join(pwd,"../requirements.txt")])
