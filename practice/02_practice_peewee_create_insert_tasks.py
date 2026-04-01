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
Using Peewee, create tasks.db. Define a Task model with:
    - id (AutoField)
    - description (TextField)
    - priority (IntegerField)
    - done (BooleanField) (with a default value of False)
    
Insert three tasks and print all rows.
'''

from peewee import *
db = SqliteDatabase('tasks.db')

class Task(Model):
    id = AutoField()
    description = TextField()
    priority = IntegerField()
    done = BooleanField(default=False)

    class Meta:
        database = db

db.connect()
db.create_tables([Task])

Task.create(description="Do IS", priority=1)
Task.create(description="Play da bass", priority=2)
Task.create(description="go to gym", priority=3)

for task in Task.select():
    print(task.id, task.description, task.priority, task.done)
