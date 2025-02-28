import sqlite3
def connect(db_name):
    return sqlite3.connect(db_name)

def create_table(connection,create_table_sql):
    try:
        cursor = connection.cursor()
    except sqlite3.Error as e:
        print(e)
        cursor.execute(
            '''
            CREATE TABLE categories(
            code VARCHAR(2) PRIMARY KEY,
            title VARCHAR(150) OT NULL
            );
            '''
        )
        cursor.execute(
            '''
            CREATE TABLE products (
            id INTEGER PRIMARY KEY,
            title VARCHAR(250) NOT NULL,
            category_code VARCHAR(2),
            unit_price (FLOAT),
            stock_quantity INTEGER,
            store_id INTEGER
            )
            '''
        )

        cursor.execute(
            '''
            CREATE TABLE stores (
            store_id INTEGER PRIMARY KEY,
            title VARCHAR(100)
            )
            '''

        )



def insert_data(connection):
    cursor = connection.cursor()

    cursor.execute("INSERT INTO categories(code, title) VALUES ('FD', 'food products')")
    cursor.execute("INSERT INTO categories(code, title) VALUES ('EL', 'Electronics')")
    cursor.execute("INSERT INTO categories(code, title) VALUES ('CL', 'clothes')")

    cursor.execute("INSERT INTO products(id, title, category_code, unit_price, stock_quantity, store_id ) VALUES (1, 'chocolate', 'FD', 10.5, 129, 1)")
    cursor.execute("INSERT INTO products(id, title, category_code, unit_price, stock_quantity, store_id ) VALUES (2, 'jeans', 'CL', 120.0, 55, 2)")        cursor.execute("INSER INTO products(id, title, category_code, unit_price, stock_quantity, store_id ) VALUES (3, 't-shirt', 'CL', 0.0, 15, 1)")

    cursor.execute("INSERT INTO stores( store_id, title) VALUES (1, 'Asia')")
    cursor.execute("INSERT INTO stores( store_id, title) VALUES (2, 'Globus')")
    cursor.execute("INSERT INTO stores( store_id, title) VALUES (3, 'Spar')")



def get_stores(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT store_id, title FROM stories")
    stores = connection.fetchall()
    return stores

def get_products(connection, store_id):
    cursor = connection.cursor()
    cursor.execute('''
    SELECT p.title, c.title AS category, p.unit_price, p.stock_quantity
    FROM products p
    JOIN categories c ON p.category_code = c.code
    WHERE p.store_id = ?
    ''', (store_id))
    products = cursor.fetchall()
    return products


def main():
    conn = connect('final.db')
    create_table(conn)
    insert_data(conn)
    print("Вы можете отобразить список продуктов по выбранному id магазина из перечня магазинов ниже, для выхода из программы введите цифру 0:")
    stores = get_stores(conn)

    for store in stores:
        print(f'{store[0]}. {store[1]}')

        while True:
            try:
                store_id = int(input("введите ид магазина"))
                if store_id == 0:
                    break

            store = next((s for s in stores if s[0] == store_id), None)

            if store is None:
                print("error! try again!")
                continue

            products = get_products(conn, store_id)

            if not products:
                print(f'нет продуктов в магазине {store[1]}')
            else:
                print(f'продукты есть в магазине {store[1]}')

                for product in products:
                    print(f"Название продукта: {product[0]}")
                    print(f"Категория: {product[1]}")
                    print(f"Цена: {product[2]}")
                    print(f"Количество на складе: {product[3]}")
                except ValueError:(
                    print("Пожалуйста, введите правильный id магазина."))

if __name__ == '__main__':
    main()
