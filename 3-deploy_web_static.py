#!/usr/bin/python3
"""Module carries out full deployment of an archive to the web servers."""
import os.path
import time
from fabric.api import env, local, put, run

env.hosts = ['100.26.241.177', '54.158.210.1']
env.user = 'ubuntu'


def do_pack():
    """Function that generates tgz archive from web_static folder"""
    dt = datetime.utcnow()
    f_name = "versions/web_static_{}{}{}{}{}{}.tgz".format(dt.year,
                                                           dt.month,
                                                           dt.day,
                                                           dt.hour,
                                                           dt.minute,
                                                           dt.second)
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(f_name)).failed is True:
        return None
    return f_name


def do_deploy(archive_path):
    """Function distributes archive to the web servers"""
    if os.path.isfile(archive_path) is False:
        return False

    file = archive_path.split("/")[-1]
    name = file.split(".")[0]

    if put(archive_path, "/tmp/{}".format(file)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/".
           format(name)).failed is True:
        return False
    if run("mkdir -p /data/web_static/releases/{}/".
           format(name)).failed is True:
        return False
    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
           format(file, name)).failed is True:
        return False
    if run("rm /tmp/{}".format(file)).failed is True:
        return False
    if run("mv /data/web_static/releases/{}/web_static/* "
           "/data/web_static/releases/{}/".format(name, name)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/web_static".
           format(name)).failed is True:
        return False
    if run("rm -rf /data/web_static/current").failed is True:
        return False
    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
           format(name)).failed is True:
        return False
    return True


def deploy():
    """Function creates and distributes an archive to web servers"""
    try:
        a_path = do_pack()
        return do_deploy(a_path)
    except Exception:
        return False
