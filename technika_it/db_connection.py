import psycopg2
from psycopg2 import OperationalError
from decouple import config


def create_connection(db_name, db_user, db_password, db_host, db_port):
    connection = None
    try:
        connection = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
        )
        print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection


def create_database(connection, query):
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Query executed successfully")
    except OperationalError as e:
        print(f"The error '{e}' occurred")


def execute_query(connection, query):
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Query executed successfully")
    except OperationalError as e:
        print(f"The error '{e}' occurred")



# connection = create_connection(
#     "postgres", config('DB_USER'), config('DB_PASSWORD'), config('DB_HOST'), ''
# )

# create_database_query = "CREATE DATABASE technika_it"
# create_database(connection, create_database_query)

connection = create_connection(
    config('DB_NAME'), config('DB_USER'), config('DB_PASSWORD'), config('DB_HOST'), ''
)


# delete_comment = "DROP TABLE client_app_product"
# execute_query(connection, delete_comment)
# delete_comment = "DROP TABLE client_app_image_product"
# execute_query(connection, delete_comment)
# delete_comment = "DROP TABLE client_app_category_product"
# execute_query(connection, delete_comment)


create_image_table = """
CREATE TABLE IF NOT EXISTS client_app_image (
    image_id INTEGER PRIMARY KEY,
    url TEXT, 
    alt VARCHAR(100)
)
"""

create_manufacture_table = """
CREATE TABLE IF NOT EXISTS client_app_manufacture (
    manufacture_id INTEGER PRIMARY KEY, 
    title VARCHAR(100)
)
"""

create_category_table = """
CREATE TABLE IF NOT EXISTS client_app_category (
    category_id INTEGER PRIMARY KEY, 
    title VARCHAR(75)
)
"""

create_product_table = """
CREATE TABLE IF NOT EXISTS client_app_product (
    product_id INTEGER PRIMARY KEY, 
    main_image_id INTEGER,
    main_category_id INTEGER,
    manufacturer_id INTEGER,
    title VARCHAR(75),
    description TEXT,
    price INTEGER,
    number_of_available INTEGER,

    CONSTRAINT fk_main_image_id
        FOREIGN KEY(main_image_id) 
        REFERENCES client_app_image(image_id),

    CONSTRAINT fk_main_category_id
        FOREIGN KEY(main_category_id) 
        REFERENCES client_app_category(category_id),

    CONSTRAINT fk_manufacturer_id
        FOREIGN KEY(manufacturer_id) 
        REFERENCES client_app_manufacture(manufacture_id)
)
"""

create_image_product_table = """
CREATE TABLE IF NOT EXISTS client_app_image_product (
    id SERIAL NOT NULL PRIMARY KEY,
    image_id INTEGER, 
    product_id INTEGER,

    CONSTRAINT fk_image_id
        FOREIGN KEY(image_id) 
        REFERENCES client_app_image(image_id),

    CONSTRAINT fk_product_id
        FOREIGN KEY(product_id) 
        REFERENCES client_app_product(product_id)
)
"""

create_category_product_table = """
CREATE TABLE IF NOT EXISTS client_app_category_product (
    id SERIAL NOT NULL  PRIMARY KEY,
    category_id INTEGER, 
    product_id INTEGER,

    CONSTRAINT fk_category_id
        FOREIGN KEY(category_id) 
        REFERENCES client_app_category(category_id),

    CONSTRAINT fk_product_id
        FOREIGN KEY(product_id) 
        REFERENCES client_app_product(product_id)
)
"""

execute_query(connection, create_image_table)
execute_query(connection, create_manufacture_table)
execute_query(connection, create_category_table)
execute_query(connection, create_product_table)
execute_query(connection, create_image_product_table)
execute_query(connection, create_category_product_table)


categories = [
    (1, "Ноутбуки"),
    (2, "Компьютеры"),
    (3, "Процессоры"),
    (4, "Материнские платы"),
    (5, "Видеокарты"),
    (6, "Оперативная память"),
    (7, "Жесткие диски"),
    (8, "Мониторы"),
    (9, "Блоки питания"),
    (10, "Аксессуары")
]
imgs = [
    (1, "https://items.s1.citilink.ru/1891570_v01_b.jpg", "something aaa")
]
manufacturers = [
    (1, "Acer")
]
products = [
    (1, 1, 1, 1, "Acer Aspire 3", '15.6", IPS, Intel Core i3 1215U 1.2ГГц, 8ГБ, 256ГБ SSD, Intel UHD Graphics , Windows 11 Home, серебристый', 49990, 5)
]

categories_records = ", ".join(["%s"] * len(categories))
imgs_records = ", ".join(["%s"] * len(imgs))
manufacturers_records = ", ".join(["%s"] * len(manufacturers))
products_records = ", ".join(["%s"] * len(products))

insert_query = (
    f"INSERT INTO client_app_category (category_id, title) VALUES {categories_records}",
    f"INSERT INTO client_app_image (image_id, url, alt) VALUES {imgs_records}",
    f"INSERT INTO client_app_manufacture (manufacture_id, title) VALUES {manufacturers_records}",
    f"INSERT INTO client_app_product (product_id, main_image_id, main_category_id, manufacturer_id, title, description, price, number_of_available) VALUES {products_records}"
)

connection.autocommit = True
cursor = connection.cursor()
cursor.execute(insert_query[0], categories)
cursor.execute(insert_query[1], imgs)
cursor.execute(insert_query[2], manufacturers)
cursor.execute(insert_query[3], products)
