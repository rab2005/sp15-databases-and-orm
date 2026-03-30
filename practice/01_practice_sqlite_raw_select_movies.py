'''
OPTIONAL AI GUIDANCE PROMPT
---------------------------
I am a student in an introductory Python class. I am learning many coding
principles for the very first time. I am going to paste in the instructions
to a practice problem that my professor gave me to try before class.
Please be my kind tutor and walk me through how to solve the problem step
by step.

Don't just give me the full solution all at once (unless I later ask for
it). Instead, help me work through it gradually, with clear explanations
and small, easy-to-understand examples. Please use everyday language and
explain things in a simple, friendly way.

INSTRUCTIONS:
-------------
Connect to movies.db and select all movie titles where rating is greater than
8.5. Print each title. Do not modify the database.

HINT: This is directly connecting to the database using the sqlite3 library.
You can use the SQL code "SELECT title FROM Movie WHERE rating > 8.5;" to get
the data you need. We won't be focusing on using SQL code in this class, but
it is good to know that you can use it.
'''
import sqlite3
conn = sqlite3.connect("movies.db")
cursor = conn.cursor()

cursor.execute("SELECT title FROM Movie WHERE rating > 8.5;")
results = cursor.fetchall()

for row in results:
    print(row[0])

conn.close()