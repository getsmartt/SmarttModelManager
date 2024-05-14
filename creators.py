import sqlite3
from contextlib import closing


def add_creator(creator_parameters):
    try:
        with closing(sqlite3.connect("manager")) as connection:
            with closing(connection.cursor()) as cursor:
                query = "INSERT OR IGNORE INTO main.creators (id, username, url, image, json) VALUES (?,?,?,?,?);"
                cursor.execute(query, creator_parameters)
                connection.commit()
                return "Success"

    except sqlite3.Error as error:
        return "Failed to insert Creator into manager", error.sqlite_errorname
