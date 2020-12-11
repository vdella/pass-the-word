import psycopg2

connection = psycopg2.connect(database='postgres', user='postgres', password='postgres', host='localhost', port='5432')
cur = connection.cursor()


def create_user(name: str, password: str):
    cur.execute('''INSERT INTO "user" (NAME, PASSWORD) VALUES (%s, %s)''', (name, password))
    connection.commit()


def check_user(name: str):
    """Fetches all users inside the registry and checks, for each,
    the username attribute.
    :param name: as the wanted username to be searched.
    :return: user's data tuple, if found, or None, if not.
    """
    cur.execute('''SELECT USER_ID, NAME, PASSWORD FROM "user"''')
    rows = cur.fetchall()
    for row in rows:
        if str(row[1]) == name:
            return row[0], row[1], row[2]
    return None


def create_label(name: str, content: str, user_id: int) -> ():
    cur.execute('''INSERT INTO "labels" (NAME, CONTENT, USER_ID) VALUES (%s, %s, %s)''',
                (name, content, user_id))
    connection.commit()


def retrieve_labels(user_id: int) -> dict:
    """Fetches all rows inside "labels" database and retrieves only
    those related to the given user id.
    :return: the user label dictionary.
    """
    user_label_table = dict()
    cur.execute('''SELECT USER_ID, NAME, CONTENT FROM "labels"''')
    rows = cur.fetchall()
    for row in rows:
        if user_id == row[0]:
            user_label_table[row[1]] = row[2]
    return user_label_table
