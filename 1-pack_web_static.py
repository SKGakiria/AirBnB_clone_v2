#!/usr/bin/python3
"""Module to compress the contents of the web_static folder."""
from fabric.api import local
from time import strftime


def do_pack():
    """Function that generates tgz archive from web_static folder"""
    try:
        local("mkdir -p versions")
        local("tar -cvzf versions/web_static_{}.tgz web_static/".
              format(time.strftime("%Y%m%d%H%M%S")))
        return ("versions/web_static_{}.tgz".format(time.
                strftime("%Y%m%d%H%M%S")))
    except Exception:
        return None
