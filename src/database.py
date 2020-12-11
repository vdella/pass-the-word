import psycopg2

connection = psycopg2.connect(database='postgres', user='postgres', password='postgres', host='localhost', port='5432')
cur = connection.cursor()


def create_user(name: str, password: str):
    with open('../user_id.txt', 'r') as f:
        user_id: int = int(f.read())
    with open('../user_id.txt', 'w') as f:
        updated_user_id = user_id + 1
        f.write(str(updated_user_id))
    cur.execute('''INSERT INTO "user" (USER_ID, NAME, PASSWORD) VALUES (%s, %s, %s)''', (user_id, name, password))
    connection.commit()


def check_user(name: str):
    cur.execute('''SELECT USER_ID, NAME, PASSWORD FROM "user"''')
    rows = cur.fetchall()
    for row in rows:
        if str(row[1]) == name:
            return row[0], row[1], row[2]
    return None


def create_label(name: str, content: str, user_id: int):
    with open('../label_id.txt', 'r') as f:
        label_id: int = int(f.read())
    with open('../label_id.txt', 'w') as f:
        updated_label_id = label_id + 1
        f.write(str(updated_label_id))
    cur.execute('''INSERT INTO "labels" (LABEL_ID, NAME, CONTENT, USER_ID) VALUES (%s, %s, %s, %s)''',
                (label_id, name, content, user_id))
    connection.commit()


def retrieve_labels(user_id: int) -> dict:
    user_label_table = dict()
    cur.execute('''SELECT USER_ID, NAME, CONTENT FROM "labels"''')
    rows = cur.fetchall()
    for row in rows:
        if user_id == row[0]:
            user_label_table[row[1]] = row[2]
    return user_label_table
