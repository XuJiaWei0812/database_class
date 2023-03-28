# 示範案例 select
import dbc

db = dbc.Database()

db.set_table('test_table')

rows = db.select(columns="name,age", where="age='40'" ,order_by="name desc",fetchone=True)
for row in rows:
    print(row)

del db