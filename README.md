# database_class
## 功能介紹
Database 是一個 Python 類別，提供了簡化 Python 與 MySQL 資料庫之間的互動。透過 Database 類別，使用者可以輕鬆地進行資料庫操作，例如：新增、查詢、更新、刪除等功能。

## 系統需求
```bash
Python 3.x
pymysql 模組
```

## 使用方法
```python
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
db.update(set_values='col1="new_value"', where='col2="value2"')

# 刪除資料
db.delete(where='col1="new_value"')
```

## 資料庫設定
此專案使用 property_helper 模組來獲取資料庫設定。在 system.ini 檔案中，您可以設定以下屬性：

host: 資料庫主機名稱或 IP 位址。

user: 資料庫使用者名稱。

password: 資料庫使用者密碼。

db: 資料庫名稱。

## 結論
Database 類別提供了簡單易用的介面，讓使用者可以輕鬆地進行資料庫操作。
