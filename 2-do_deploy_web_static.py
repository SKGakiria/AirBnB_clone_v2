#!/usr/bin/python3
"""Module to deploy an archive to the web servers."""
from fabric.api import env
from fabric.api import put
from fabric.api import run
from datetime import datetime
from os import path

env.hosts = ['100.26.241.177', '54.158.210.1']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """Function distributes archive to the web servers"""
    if not (path.exists(archive_path)):
        return False

    try:
        put(archive_path, '/tmp/')

        timestamp = archive_path[-18:-4]
        run('sudo mkdir -p /data/web_static/\
releases/web_static_{}/'.format(timestamp))

        run('sudo tar -xzf /tmp/web_static_{}.tgz -C \
/data/web_static/releases/web_static_{}/'
                    .format(timestamp, timestamp))

        run('sudo rm /tmp/web_static_{}.tgz'.format(timestamp))

        run('sudo mv /data/web_static/releases/web_static_{}/web_static/* \
/data/web_static/releases/web_static_{}/'.format(timestamp, timestamp))

        run('sudo rm -rf /data/web_static/releases/\
web_static_{}/web_static'
                    .format(timestamp))

        run('sudo rm -rf /data/web_static/current')

        run('sudo ln -s /data/web_static/releases/\
web_static_{}/ /data/web_static/current'.format(timestamp))
    except:
        return False

    return True
