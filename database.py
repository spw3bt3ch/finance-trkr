import sqlite3

conn = sqlite3.connect('users.db')
cur = conn.cursor()

# print('Database created successfully')

# cur.execute("""CREATE TABLE IF NOT EXISTS registration (
#             fullname TEXT NOT NULL, email_address TEXT NOT NULL, mobile_number INTEGER NOT NULL, username TEXT NOT NULL, password TEXT NOT NULL
#             )""")
# print('Table created successfully')

# cur.execute("""CREATE TABLE IF NOT EXISTS contact(fullname TEXT NOT NULL, email TEXT NOT NULL, phone TEXT NOT NULL, message TEXT NOT NULL)""")
# print('Table created successfully')

conn.close()

