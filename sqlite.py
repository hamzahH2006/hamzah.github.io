import sqlite3

# الاتصال بقاعدة البيانات
conn = sqlite3.connect('users.db')

# إنشاء كائن من أجل تنفيذ الأوامر
cursor = conn.cursor()

# تنفيذ استعلام SQL للحصول على البيانات
cursor.execute("SELECT * FROM users")

# جلب جميع النتائج
rows = cursor.fetchall()

for row in rows:
    print(row)

# غلق الاتصال بقاعدة البيانات
conn.close()
