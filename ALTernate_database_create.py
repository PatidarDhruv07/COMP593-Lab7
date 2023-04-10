import sqlite3
import random
from faker import Faker
import datetime

# Connection to a database
conn = sqlite3.connect('people.db')

# Cursor object
c = conn.cursor()

# People table created
c.execute('''
    CREATE TABLE people (
        id INTEGER PRIMARY KEY,
        first_name TEXT,
        last_name TEXT,
        age INTEGER,
        email TEXT,
        created_at TEXT,
        updated_at TEXT
    )
''')

# Populate the people table with 200 fake people
fake = Faker()
for i in range(200):
    first_name = fake.first_name()
    last_name = fake.last_name()
    age = random.randint(1, 100)
    email = fake.email()
    created_at = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    updated_at = created_at
    c.execute('''
        INSERT INTO people (first_name, last_name, age, email, created_at, updated_at)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (first_name, last_name, age, email, created_at, updated_at))

# Close the connection
conn.close()

# Commit the changes
conn.commit()
