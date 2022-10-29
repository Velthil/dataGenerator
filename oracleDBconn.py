import cx_Oracle


class DbConnection:
    def __init__(self):
        self._conn = cx_Oracle.connect('SYSTEM/Traktor0@localhost')
        self._cursor = self._conn.cursor()
        print('DB connected')

    def __del__(self):
        self._cursor.close()
        self._conn.close()
        print('DB closed')

    def execute(self, sql, params=None):
        return self._cursor.execute(sql, params or ())

    def commit(self):
        self._conn.commit()
