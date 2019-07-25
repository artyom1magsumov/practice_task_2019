def get_state(user_id, cursor):
    cursor.execute('SELECT State FROM Users WHERE user_id=' +
                   str(user_id))
    a = cursor.fetchone()
    if a is None:
        return -1
    else:
        return a[0][0]


def set_state(user_id, state, cursor, db):
    cursor.execute('UPDATE Users SET State=' + str(state) +
                   ' WHERE user_id=' +str(user_id))
    db.commit()


def add_user(counter, user_id, name, cursor, db):
    cursor.execute(f"INSERT OR IGNORE INTO Users (counter, user_id, name) VALUES ({counter}, {user_id}, {name}")
    db.commit()


def add_stat(name_stat, cursor, db):
    cursor.execute(f"INSERT INTO Stats (name_stat) VALUES ('{name_stat}')")
    db.commit()


def insert_name_stat(number_stat, cursor, db):
    cursor.execute(
        f"UPDATE Users SET name_stat=(SELECT name_stat FROM Stats WHERE number_stat = '{number_stat}') "
        f"WHERE number_stat='{number_stat}'")
    db.commit()


def get_stats_list(cursor):
    cursor.execute(f"SELECT * FROM Stats")
    return cursor.fetchall()


def number_stats(cursor):
    cursor.execute(f"SELECT COUNT (number) FROM Stats")
    return cursor.fetchall()


def add_stat_value(number_stats, cursor, db):
    cursor.execute(f"UPDATE OR IGNORE Users SET number_stat={number_stat} WHERE user_id={user_id}")
    cursor.execute(f"INSERT OR IGNORE Stats (user_id, number_stat, stat_value) VALUES ({user_id}, {number_stat}, {stat_value})")
    db.commit()


def get_name_stat(number, cursor):
    cursor.execute(f"SELECT name_stat FROM Stats WHERE number={number} ")
    return str(cursor.fetchall())[2:-3]


def get_stat_value(user_id, number_stats, cursor, db):
    cursor.execute(f"Select stat_value FROM Stats (user_id, name_stat, stat_value) VALUES ({user_id}, {number_stat}, {stat_value})")
    db.commit()


def insert_name_of_user(user_id, name, cursore, db):
    cursore.execute(f"UPDATE Users SET name='{name}'  WHERE user_id={user_id}")
    db.commit()


def get_name_stat_from_user(user_id, cursor):
    cursor.execute(f"SELECT name_stat FROM Users WHERE user_id={user_id}")
    return str(cursor.fetchall())[2:-3]