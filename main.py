import pymysql
import configparser

class Database:

    def __init__(self):
        config = configparser.ConfigParser()
        config .read('system.ini')
        self.host = config.get('db_setting', 'host')
        self.user = config.get('db_setting', 'user')
        self.password = config.get('db_setting', 'password')
        self.database = config.get('db_setting', 'db')
        self.conn = pymysql.connect(host=self.host, user=self.user, password=self.password, db=self.database)
        self.cur = self.conn.cursor()
        self.table_name = None

    def set_table(self, table_name):
        self.table_name = table_name

    def insert(self, **kwargs):
        keys = list(kwargs.keys())
        values = tuple(kwargs.values())
        placeholders = ', '.join(['%s'] * len(keys))
        columns = ', '.join(keys)
        query = f"INSERT INTO {self.table_name} ({columns}) VALUES ({placeholders})"
        self.cur.execute(query, values)
        self.conn.commit()

    def select(self, columns='*', where='', order_by='', limit='', fetchone=False):
        query = f"SELECT {columns} FROM {self.table_name}"
        if where:
            query += f" WHERE {where}"
        if order_by:
            query += f" ORDER BY {order_by}"
        if limit:
            query += f" LIMIT {limit}"
        self.cur.execute(query)
        if fetchone:
            return self.cur.fetchone()
        else:
            return self.cur.fetchall()

    def update(self, set_values, where=None):
        query = f"UPDATE {self.table_name} SET {set_values}"
        if where is not None:
            query += f" WHERE {where}"
        self.cur.execute(query)
        self.conn.commit()

    def delete(self, where=None):
        query = f"DELETE FROM {self.table_name}"
        if where is not None:
            query += f" WHERE {where}"
        self.cur.execute(query)
        self.conn.commit()

    def __del__(self):
        self.conn.close()