import sqlite3
import random
from faker import Faker
import datetime
import pandas as pd

def main():
    create_people_table()
    query_old_people()


def create_people_table():
    # Create a database connection
    conn = sqlite3.connect('people.db')

    # Create a cursor object
    c = conn.cursor()

    # Create the people table
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

    # Commit the changes
    conn.commit()

    # Close the connection
    conn.close()


def query_old_people():
    # Create a database connection
    conn = sqlite3.connect('people.db')

    # Create a cursor object
    c = conn.cursor()

    # Query the database for old people
    c.execute('SELECT first_name, last_name, age FROM people WHERE age >= 50')
    old_people = c.fetchall()

    # Print the names and ages of old people
    for person in old_people:
        print(f'{person[0]} {person[1]} is {person[2]} years old.')

    # Save old people to a CSV file
    df = pd.DataFrame(old_people, columns=['first_name', 'last_name', 'age'])
    df.to_csv('old_people.csv', index=False)

    # Close the connection
    conn.close()



if __name__ == '__main__':
    main()
