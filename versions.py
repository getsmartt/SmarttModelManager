import sqlite3
from contextlib import closing


def add_version(version_parameters):
    try:
        with closing(sqlite3.connect('manager')) as connection:
            with closing(connection.cursor()) as cursor:
                query = ("INSERT OR REPLACE INTO versions (id, name, description, modelid, created, url, words, hash, "
                         "downloads, ratings, rating, updated, basemodel, json, deployed, vault, localpath, localname, "
                         "added, filename, status, lastupdated, published, lastchecked, nsfw, updateavailable, "
                         "thumbsup, thumbsdown, originalname, originalpath) "
                         "VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);")
                cursor.execute(query, version_parameters)
                connection.commit()
                return 'Success'

    except sqlite3.Error as error:
        return "Failed to insert Version into manager. ERROR: " + error.sqlite_errorname


# get version path by hash
def get_path_by_hash(h):
    with closing(sqlite3.connect("manager")) as connection:
        with closing(connection.cursor()) as cursor:
            query = "SELECT v.localpath FROM versions v where v.hash = ?"
            cursor.execute(query, h)
            row = cursor.fetchone()
            if row is not None:
                return row[0]
            else:
                return False
