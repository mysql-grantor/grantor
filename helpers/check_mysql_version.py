#!/usr/bin/env python3
#encoding: utf8

import pymysql
from helpers.common import *

def check_mysql_version(conn, local_mysql_version_file):
    cur = conn.cursor()
    cur.execute('SHOW VARIABLES LIKE "version"')
    version = cur.fetchall()[0][1].split('-')[0]

    if os.path.isfile(local_mysql_version_file):
        git_mysql_version = quick_read(local_mysql_version_file).split('-')[0]
    else:
        logv("warning: no mysql_version file")
        return True

    logv("target mysql version:%s / running mysql version: %s" % (git_mysql_version, version))

    return version == git_mysql_version
