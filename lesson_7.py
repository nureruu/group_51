import sqlite3
def create_connection(db_name):
    connecton = None
    try:
        connecton = sqlite3.connect(db_name)
    except sqlite3.Error as e:
        print(e)

    return connecton

def create_table(connection,create_table_sql):
    try:
        cursor = connection.cursor()
        cursor.execute(create_table_sql)
    except sqlite3.Error as e:
        print(e)

db_name = '''group_51.db'''
sql_to_create_employees_table ='''
CREATE TABLE employees(
id, INTEGER PRIMARY KEY AUTOINCREMENT,
full_name VARCHAR(200) NOT NULL, 
salary FLOAT DEFAULT 0.0, 
hobby  TEXT DEFAULT NULL,
birth_date DATE NOT NULL,
is_married BOOLEAN DEFAULT FALSE
)
'''
my_connection = create_connection(db_name)
if my_connection is not None:
    print('Connecting')
    create_table(my_connection, sql_to_create_employees_table)
    my_connection.close()








