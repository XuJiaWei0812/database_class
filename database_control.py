import pymysql
import property_helper


class Database:

    def __init__(self):
        self.host = property_helper.get_property('db_setting', 'host')
        self.user = property_helper.get_property('db_setting', 'user')
        self.password = property_helper.get_property('db_setting', 'password')
        self.database = property_helper.get_property('db_setting', 'db')
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

    def update(self, set_values, conditions=None):
        query = f"UPDATE {self.table_name} SET {set_values}"
        if conditions is not None:
            query += f" WHERE {conditions}"
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

# 使用方式:

# 1.初始化資料庫連線
# db = Database()

# 2.設置要使用的資料表
# db.set_table('test_table')

# 3.使用CRUD Function
# 3-1.insert 參數就是你要填入的欄位
# db.insert(name='kamigo', age=65)

# 3-2.select 參數的 columns是欄位 where 是條件 order_by 是排序 fetchone是判斷全部拿取跟單獨拿取
# rows = db.select(columns="name,age", where="age='40'" ,order_by="name desc",fetchone=True)
# for row in rows:
#     print(row)

# 3-3.update 參數的 set_values 是要更改的欄位跟值 where 是條件
# db.update(set_values="age=35", where="name='John'")

# 3-4.delete 參數的 where是條件
# db.delete(where="age < 25")

# 4.關閉資料庫連線
# del db
