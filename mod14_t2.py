import sqlite3

connection = sqlite3.connect('not_telegram2.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

cursor.execute('CREATE INDEX IF NOT EXISTS idx_email ON Users (email)')

for i in range(1, 11):
    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ? ,?)',
                   (f'newuser{i}', f'example{i}@gmail.com', f'{10*i}', '1000'))

for i in range(1, 11, 2):
    cursor.execute('UPDATE Users SET balance = ? WHERE username = ?', (500, f'newuser{i}'))

for i in range(1, 11, 3):
    cursor.execute('DELETE FROM Users WHERE username = ?', (f'newuser{i}',))

cursor.execute('SELECT * FROM Users WHERE age != 60')
users = cursor.fetchall()
for i in users:
    print(f'Имя: {i[1]} | Почта: {i[2]} | Возраст: {i[3]} | Баланс: {i[4]}')

cursor.execute('DELETE FROM Users WHERE id = ?', (6,))

cursor.execute('SELECT COUNT (*) FROM Users')
total = cursor.fetchone()[0]
print(total)

cursor.execute('SELECT SUM(balance) FROM Users')
total2 = cursor.fetchone()[0]
print(total2)

cursor.execute('SELECT AVG(balance) FROM Users')
total3 = cursor.fetchone()[0]
print(total3)

connection.commit()
connection.close()
