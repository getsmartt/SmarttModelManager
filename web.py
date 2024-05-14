import os
import sqlite3
from contextlib import closing
from os.path import exists
from pathlib import Path


def get_version(version):
    with closing(sqlite3.connect("manager")) as connection:
        with closing(connection.cursor()) as cursor:
            version_sql = "SELECT * FROM main.v_view where version_id=?"
            rows = cursor.execute(version_sql, (version,)).fetchall()
            desc = cursor.description
            column_names = [col[0] for col in desc]
            data = [dict(zip(column_names, row))
                    for row in rows]
    return data
