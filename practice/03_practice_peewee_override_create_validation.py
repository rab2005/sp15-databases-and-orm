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
Create a simple task manager using Peewee and SQLite.

1. Import everything from the peewee library using: from peewee import *

2. Create a database using:
   db = SqliteDatabase('tasks.db')

3. Define a Task model that inherits from Model. It should include:
   - An AutoField for the task id
   - A TextField for the task description
   - An IntegerField for the priority
   - A BooleanField for whether the task is done (default should be False)

4. Inside the Task class, define a Meta class and set database = db

5. Add a class method called create that:
   - Accepts keyword arguments (**query)
   - Checks if the 'priority' is between 1 and 5
   - If it's not, print a message and return None
   - If it is, call super().create(**query) to add the task

6. Connect to the database with db.connect()

7. Create the tasks table using:
   db.create_tables([Task])

8. Try to create two tasks using Task.create():
   - One with a priority that is not valid (like 9)
   - One with a valid priority (like 5)

9. Loop through all tasks using Task.select() and print the task id,
   description, and priority for each one
'''

import peewee as p

db = p.SqliteDatabase("dogs.db")

class Dog(p.Model):
    dog_id = p.AutoField(primary_key=True)
    name = p.CharField()
    age = p.IntegerField()
    fav_food = p.CharField(null=True)
    
    class Meta:
        database = db

db.connect()

db.drop_tables([Dog])   # drop old table so schema stays fresh
db.create_tables([Dog])

dog1 = Dog.create(name="Sally", age=2, fav_food="yum")
dog2 = Dog.create(name="Sjosy", age=2, fav_food="yum")

# Read
all_dogs = Dog.select()
for dog_obj in all_dogs:
    print(f"{dog_obj.name} is {dog_obj.age}")

# Update Sally's favorite food
Dog.update(fav_food="bones").where(Dog.name == "Sally").execute()
print(f"\nUpdated Sally's favorite food to bones")

# Delete Sjosy
Dog.delete().where(Dog.name == "Sjosy").execute()
print(f"Deleted Sjosy from the database")

# Read again to confirm changes
print("\nDogs after update and delete:")
for dog_obj in Dog.select():
    print(f"{dog_obj.name} is {dog_obj.age}, favorite food: {dog_obj.fav_food}")

db.close()