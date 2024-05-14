import sqlite3
from contextlib import closing

# get tagid by tagname

# get tagname by tagid


def add_tag(tag_parameters):
    with closing(sqlite3.connect('manager')) as connection:
        connection.row_factory = sqlite3.Row
        with closing(connection.cursor()) as cursor:
            query = "SELECT id FROM main.tags WHERE tagname = ?"
            cursor.execute(query, tag_parameters)
            row = cursor.fetchone()
            if row is not None:
                return row['id']
            else:
                try:
                    with closing(sqlite3.connect("manager")) as connection2:
                        with closing(connection2.cursor()) as cursor2:
                            query = "INSERT OR IGNORE INTO main.tags (tagname) VALUES (?);"
                            cursor2.execute(query, tag_parameters)
                            connection2.commit()                            # cursor.close()
                            cursor2.execute("SELECT last_insert_rowid()")
                            row = cursor2.fetchall()
                            return row[0][0]

                except sqlite3.Error as error:
                    return "Failed to insert Tag into manager. ERROR: " + error.sqlite_errorname

# create tag alias

# block tag

# delete tag

# delete tag from model


def add_tag2model (tag_id, model_id):

    try:
        with closing(sqlite3.connect("manager")) as connection:
            with closing(connection.cursor()) as cursor:
                query = "INSERT OR IGNORE INTO main.model2tag (modelid, tagid) VALUES (?,?);"
                parameters = (model_id, tag_id)
                cursor.execute(query, parameters)
                connection.commit()
                return 'Success'

    except sqlite3.Error as error:
        return "Failed to insert Tag into manager. ERROR: " + error.sqlite_errorname



# get tags by model

# get all tags

# merge tags

# rename tag
