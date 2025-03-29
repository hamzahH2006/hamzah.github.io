from flask import Flask, request, jsonify
from flask_cors import CORS  # استيراد مكتبة CORS
import sqlite3

app = Flask(__name__)
CORS(app)  # تفعيل CORS على التطبيق بأكمله

# إضافة بيانات المستخدم إلى قاعدة البيانات
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    try:
        # الاتصال بقاعدة البيانات
        conn = sqlite3.connect('users.db')
        c = conn.cursor()

        # التأكد من وجود جدول المستخدمين
        c.execute('''CREATE TABLE IF NOT EXISTS users
                     (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, email TEXT, password TEXT)''')
        
        # إضافة بيانات المستخدم
        c.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)", 
                  (username, email, password))

        # حفظ التغييرات
        conn.commit()
        conn.close()

        return jsonify({"message": "User registered successfully!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# تشغيل السيرفر
if __name__ == '__main__':
    app.run(debug=True)
