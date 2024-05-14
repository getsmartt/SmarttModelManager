import sqlite3
from contextlib import closing


def dump_sql():
    db_filename = 'manager'
    newline_indent = '\n   '

    db = sqlite3.connect(db_filename)
    db.text_factory = str
    cur = db.cursor()

    result = cur.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
    table_names = sorted(list(zip(*result))[0])
    print("\ntables are:" + newline_indent + newline_indent.join(table_names))

    for table_name in table_names:
        result = cur.execute("PRAGMA table_info('%s')" % table_name).fetchall()
        column_names = list(zip(*result))[1]
        print(("\ncolumn names for %s:" % table_name)
              + newline_indent
              + (newline_indent.join(column_names)))

    db.close()
    print("\nexiting.")


# get model name by model id

# get model id by model name

# get models by tag


def add_model(m_id, name, description, m_type, nsfw, mode, json, source, creator_id, updateavailable, lastupdated):
    try:
        with closing(sqlite3.connect("manager")) as connection:
            with closing(connection.cursor()) as cursor:
                query = ("INSERT OR REPLACE INTO main.models (id, name, description, type, nsfw, mode, creatorid, json, "
                         "source, updateavailable, lastupdated) VALUES (?,?,?,?,?,?,?,?,?,?,?);")
                parameters = (m_id, name, description, m_type, nsfw, mode, creator_id, json, source, updateavailable,
                              lastupdated)
                cursor.execute(query, parameters)
                connection.commit()
                return 'Success'

    except sqlite3.Error as error:
        return "Failed to insert Model into manager. ERROR: " + error.sqlite_errorname


# edit model

# delete model

# get models by creator

# get models by type

# get model by version id


def get_all_models():
    with closing(sqlite3.connect("manager")) as connection:
        with closing(connection.cursor()) as cursor:
            rows = cursor.execute("SELECT * FROM main.models").fetchall()
            return rows

# get models by basemodel

# get new model id
