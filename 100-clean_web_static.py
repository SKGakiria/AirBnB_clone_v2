#!/usr/bin/python3
"""Module carries out full deployment of an archive to the web servers."""
import os
from datetime import datetime
from fabric.api import *

env.hosts = ['100.26.241.177', '54.158.210.1']
env.user = 'ubuntu'


def do_clean(number=0):
    """Function that deletes out-of-date archives"""
    number = int(number)

    if number == 0:
        number = 2
    else:
        number += 1

    local('cd versions ; ls -t | tail -n +{} | xargs rm -rf'.format(number))
    path = '/data/web_static/releases'
    run('cd {} ; ls -t | tail -n +{} | xargs rm -rf'.format(path, number))
