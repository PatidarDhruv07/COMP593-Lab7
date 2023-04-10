# I wanna try something new to do this script and after some digging i found out cursor object.
# Here is the link for that https://www.tutorialspoint.com/python_data_access/python_mysql_cursor_object.htm
# GeeksForGeeks https://www.geeksforgeeks.org/python-sqlite-cursor-object/


import sqlite3
import pandas as pd

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
