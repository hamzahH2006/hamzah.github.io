import sqlite3

# الاتصال بقاعدة البيانات (إن لم تكن موجودة سيتم إنشاؤها)
conn = sqlite3.connect('users.db')
c = conn.cursor()

# إنشاء جدول المستخدمين
c.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    password TEXT NOT NULL
)
''')

conn.commit()
conn.close()
