# pydbc
## 功能介紹
提供了簡化 Python 與 MySQL 資料庫之間的互動。透過 Database 類別，使用者可以輕鬆地進行資料庫操作，例如：新增、查詢、更新、刪除等功能。

## 系統需求
```bash
Python 3.x
pymysql 模組
```

## 使用方法
```python
# 創建 Database 類別實例
db = pydbc.Database()

# 設定使用的資料表名稱
db.set_table('table_name')

# 新增一筆資料，參數就是你要填入的欄位
db.insert(col1='value1', col2='value2')

# 查詢資料，columns是欄位名稱、where、是查詢條件、order_by 是排序方式、fetchone 是否只回傳一筆資料
result = db.select(columns="test1,test2", where="test1='40'" ,order_by="test1 desc",fetchone=True)

# 更新資料，set_values 是更新的欄位與值、where 是更新條件
db.update(set_values='col1="new_value"', where='col2="value2"')

# 刪除資料，where 是刪除條件
db.delete(where='col1="new_value"')
```

## 資料庫設定
此專案使用 configparser 模組來獲取資料庫設定。在 system.ini 檔案中，您可以設定以下屬性：

host: 資料庫主機名稱或 IP 位址。

user: 資料庫使用者名稱。

password: 資料庫使用者密碼。

db: 資料庫名稱。
