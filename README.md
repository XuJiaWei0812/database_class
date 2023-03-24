# database_class
## 功能介紹
Database 是一個 Python 類別，提供了簡化 Python 與 MySQL 資料庫之間的互動。透過 Database 類別，使用者可以輕鬆地進行資料庫操作，例如：新增、查詢、更新、刪除等功能。

## 功能介紹
```bash
Python 3.x
pymysql 模組
```

## 使用方法
```python=
# 載入 Database 類別
from database import Database

# 創建 Database 類別實例
db = Database()

# 設定使用的資料表名稱
db.set_table('table_name')

# 新增一筆資料
db.insert(col1='value1', col2='value2')

# 查詢資料
result = db.select(where='col1="value1"')

# 更新資料
db.update(set_values='col1="new_value"', conditions='col2="value2"')

# 刪除資料
db.delete(where='col1="new_value"')
```

## 函式說明
__init__()
建立與資料庫的連線，並設定預設的資料表名稱。

set_table(table_name)
設定要使用的資料表名稱。

table_name: 資料表名稱。
insert(**kwargs)
新增一筆資料。

**kwargs: 新增的資料，以欄位名稱與值的鍵值對(Key-Value Pairs)形式提供。
select(columns='*', where='', order_by='', limit='', fetchone=False)
查詢符合條件的資料。

columns: 要查詢的欄位名稱，以逗號分隔。預設值為所有欄位(*)。
where: 查詢條件，以 SQL WHERE 語法提供。預設值為空字串('')。
order_by: 查詢排序方式，以 SQL ORDER BY 語法提供。預設值為空字串('')。
limit: 查詢筆數限制，以 SQL LIMIT 語法提供。預設值為空字串('')。
fetchone: 是否只回傳一筆資料。預設值為 False。
update(set_values, conditions=None)
更新符合條件的資料。

set_values: 要更新的欄位與值，以 SQL SET 語法提供。
conditions: 更新條件，以 SQL WHERE 語法提供。預設值為 None。
delete(where=None)
刪除符合條件的資料。

where: 刪除條件，以 SQL WHERE 語法提供。預設值為 None。
__del__()
關閉與資料庫的連線。
