from pysqlite2 import dbapi2 as sqlite3

def dict_factory(cursor, row):
    d = {}
    for idx,col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

connection = sqlite3.connect('./chalicelib/database.db')
connection.row_factory = dict_factory
connection.enable_load_extension(True)
connection.load_extension("./chalicelib/libsqlitefunctions")
db = connection.cursor()

