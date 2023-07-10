#!/usr/bin/python3
"""Module carries out full deployment of an archive to the web servers."""
import os
from datetime import datetime
from fabric.api import *

env.hosts = ['100.26.241.177', '54.158.210.1']


def do_clean(number=0):
    """Function that deletes out-of-date archives"""
    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]
