import sqlite3
import database_commands

db = sqlite3.connect('Users.sqlite')
cursor = db.cursor()

cursor.execute("""CREATE TABLE Users(
counter INT PRIMARY KEY, 
user_id INTEGER NOT NULL,
name VARCHAR(30)
number_stat INTEGER
name_stat VARCHAR(30)
status INTEGER)""")

cursor.execute("""CREATE TABLE Stats(
counter INT PRIMARY KEY,
user_id INTEGER NOT NULL,
number_stat INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
name_stat VARCHAR(30)
stat_value INTEGER)""")


def add_stat(name_event, cursor, db):
    cursor.execute(f"INSERT INTO Stats (name_stat) VALUES ('{name_stat}')")
    db.commit()


database_commands.add_stat('Speed', cursor, db)
database_commands.add_stat('Performance', cursor, db)
database_commands.add_stat('Correctness', cursor, db)





db.commit()