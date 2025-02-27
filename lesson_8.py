import sqlite3

def connect_to_db(db_name):
    return sqlite3.connect(db_name)



def create_tables(conn):
    cursor = conn.cursor()


    cursor.execute(
        '''
    CREATE TABLE countries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL
    );
    ''')


    cursor.execute('''
    CREATE TABLE cities (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        area REAL DEFAULT 0,
        country_id INTEGER,
        FOREIGN KEY (country_id) REFERENCES countries(id)
    );
    ''')


    cursor.execute('''
    CREATE TABLE students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        city_id INTEGER,
        FOREIGN KEY (city_id) REFERENCES cities(id)
    );
    ''')


    conn.commit()



def insert_data(conn):
    cursor = conn.cursor()


    cursor.execute("INSERT INTO countries (title) VALUES ('Кыргызстан')")
    cursor.execute("INSERT INTO countries (title) VALUES ('Германия')")
    cursor.execute("INSERT INTO countries (title) VALUES ('Китай')")


    cursor.execute("INSERT INTO cities (title, area, country_id) VALUES ('Бишкек', 300, 1)")
    cursor.execute("INSERT INTO cities (title, area, country_id) VALUES ('Ош', 150, 1)")
    cursor.execute("INSERT INTO cities (title, area, country_id) VALUES ('Берлин', 891, 2)")
    cursor.execute("INSERT INTO cities (title, area, country_id) VALUES ('Мюнхен', 310, 2)")
    cursor.execute("INSERT INTO cities (title, area, country_id) VALUES ('Пекин', 1650, 3)")
    cursor.execute("INSERT INTO cities (title, area, country_id) VALUES ('Шанхай', 6340, 3)")
    cursor.execute("INSERT INTO cities (title, area, country_id) VALUES ('Гуанчжоу', 7434, 3)")


    cursor.execute("INSERT INTO students (first_name, last_name, city_id) VALUES ('Иван', 'Иванов', 1)")
    cursor.execute("INSERT INTO students (first_name, last_name, city_id) VALUES ('Алина', 'Петрова', 2)")
    cursor.execute("INSERT INTO students (first_name, last_name, city_id) VALUES ('Михаил', 'Смирнов', 3)")
    cursor.execute("INSERT INTO students (first_name, last_name, city_id) VALUES ('Дарина', 'Попова', 4)")
    cursor.execute("INSERT INTO students (first_name, last_name, city_id) VALUES ('Дмитрий', 'Сидоров', 5)")
    cursor.execute("INSERT INTO students (first_name, last_name, city_id) VALUES ('Оля', 'Романова', 6)")
    cursor.execute("INSERT INTO students (first_name, last_name, city_id) VALUES ('Игорь', 'Кузнецов', 7)")
    cursor.execute("INSERT INTO students (first_name, last_name, city_id) VALUES ('Марина', 'Шмидт', 2)")



    conn.commit()


def get_cities(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT id, title FROM cities")
    cities = cursor.fetchall()
    return cities



def get_students_by_city(conn, city_id):
    cursor = conn.cursor()
    cursor.execute('''
    SELECT s.first_name, s.last_name, c.title AS city, co.title AS country, ci.area
    FROM students s
    JOIN cities ci ON s.city_id = ci.id
    JOIN countries co ON ci.country_id = co.id
    WHERE ci.id = ?
    ''',
                   (city_id,))
    students = cursor.fetchall()
    return students



def main():
    conn = connect_to_db('example.db')
    create_tables(conn)
    insert_data(conn)

    print(
        "Вы можете отобразить список учеников по выбранному id города из перечня городов ниже, для выхода из программы введите 0:")

    cities = get_cities(conn)

    for city in cities:
        print(f"{city[0]} - {city[1]}")

    while True:
        try:
            city_id = int(input("Введите id города: "))

            if city_id == 0:
                print("Выход из программы.")
                break

            city = next((city for city in cities if city[0] == city_id), None)

            if city is None:
                print("Неверный id города. Попробуйте снова.")
                continue

            students = get_students_by_city(conn, city_id)

            if not students:
                print(f"Нет учеников в городе {city[1]}.")
            else:
                print(f"Ученики из города {city[1]} (площадь города {students[0][4]}):")
                for student in students:
                    print(f"Имя: {student[0]}, Фамилия: {student[1]}, Страна: {student[3]}, Город: {student[2]}")
        except ValueError:
            print("Пожалуйста, введите правильный id города.")


if __name__ == '__main__':
    main()
