#!/usr/bin/env python3
#coding: utf8

from helpers.common import *

def create_new_mysql_user():
  True

def apply_global_perms(conn, user, sql_host, global_perms_content):
    cur = conn.cursor()
    log("UPDATING permissions for %s@%s" % ( user, sql_host ))

    columns = [ 'User', 'Host' ]
    privs = [ ]
    for perm in global_perms_content:
        columns.append(perm[0])
        privs.append("'" + perm[1] + "'")

    #FIXME :  quick shit in case, those mandatory columns are not present
    default_column=['ssl_cipher','x509_issuer','x509_subject']
    for dc in default_column:
        if dc not in columns:
            columns.append(dc)
            privs.append("''")


    sql = "REPLACE INTO mysql.user ( %s ) VALUES ( '%s', '%s', %s )" %  ( ','.join(columns), user, sql_host, ','.join(privs) )
    cur.execute( sql )
