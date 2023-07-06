#!/usr/bin/python3
"""Module to compress the contents of the web_static folder."""
from fabric.api import local
from datetime import date
from time import strftime


def do_pack():
    """Function that generates tgz archive from web_static folder"""

    f_name = strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local("tar -czvf versions/web_static_{}.tgz web_static/"
              .format(f_name))

        return "versions/web_static_{}.tgz".format(f_name)

    except Exception:
        return None
