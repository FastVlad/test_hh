import sqlite3
import datetime
import random


conn = sqlite3.connect('schedule.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS schedule (
                    id INTEGER PRIMARY KEY,
                    check_date DATE
                )''')

current_date = datetime.datetime.now()

for _ in range(100):
    days_difference = random.randint(2, 7)
    new_date = current_date + datetime.timedelta(days=days_difference)
    cursor.execute("INSERT INTO schedule (check_date) VALUES (?)", (new_date.date().strftime('%d.%m.%Y'),))
    current_date = new_date

conn.commit()
conn.close()
