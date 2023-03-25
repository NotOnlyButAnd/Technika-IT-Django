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

delete_comment = "DROP TABLE client_app_image_product"
execute_query(connection, delete_comment)
delete_comment = "DROP TABLE client_app_category_product"
execute_query(connection, delete_comment)
delete_comment = "DROP TABLE client_app_product"
execute_query(connection, delete_comment)
delete_comment = "DROP TABLE client_app_image"
execute_query(connection, delete_comment)



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
    (1,"https://c.dns-shop.ru/thumb/st4/fit/300/300/36f2c767ad98f5c902dbcb6cee38b51e/43d204d624f95a8f83b8bbf33624315c4b9013149bfb6da6de4b90ab9bf73742.jpg", "something aaa"),
    (2,"https://c.dns-shop.ru/thumb/st4/fit/0/0/d28d138ac48b4d07759deac35eaf63c8/e629cf6cd47923025b0085c660818330ca293519b198543890988f13cc93d9e3.jpg.webp","IT_Boss"),
    (3,"https://c.dns-shop.ru/thumb/st4/fit/300/300/a6d30de5f8338b405e51abc59649aa20/25a9285315754663ae515ad6ccce60f5c44aabe31c0fd3b5c5b811b0bc2f1dd2.jpg","Lyaska"),
    (4,"https://items.s1.citilink.ru/1848729_v01_b.jpg","Za"),
    (5,"https://c.dns-shop.ru/thumb/st4/fit/300/300/b1af3c8ab65bab573d8ca389400c5bd1/a1896283b9f2156c31ad61dde88882ccfee2894476e184f4c72e911acf3bde87.jpg","Mashku"),
    (6,"https://c.dns-shop.ru/thumb/st4/fit/500/500/100368f9e8fbab7d83bde7d1a266428e/150d9a55fa04794593ac811d244387b6501b4e4bdd20e3725a9cfdecaa0af82a.jpg.webp","Mozno"),

]
manufacturers = [
    (1, "Acer"),
    (2, "Asus"),(3,"HP"),(4,"Lenovo"),(5,"Echips "),(6,"Dell")
]
products = [
    (1, 1, 1, 1, "Acer Aspire 3", '15.6", IPS, Intel Core i3 1215U 1.2ГГц, 8ГБ, 256ГБ SSD, Intel UHD Graphics , Windows 11 Home, серебристый', 49990, 5),
    (2,2,1,2,"ASUS Laptop 15",'15.6",Full HD (1920x1080), TN+film, Intel Celeron N4020, ядра: 2 х 1.1 ГГц, RAM 4 ГБ, HDD 1000 ГБ, Intel UHD Graphics', 22399, 10),
    (3,3,1,3,"HP 255 G8",'15.6",HD (1366x768), SVA (TN+film), AMD Athlon Gold 3150U, ядра: 2 х 2.4 ГГц, RAM 4 ГБ, HDD 1000 ГБ, AMD Radeon Graphics',32000,3),
    (4,4,1,4,"Lenovo IdeaPad 3",'15.6",HD (1366x768), TN+film, Intel Celeron N4020, ядра: 2 х 1.1 ГГц, RAM 4 ГБ, HDD 1000 ГБ, Intel UHD Graphics',25999,13),
    (5,5,1,5,"Echips Envy ",'15.6",Full HD (1920x1080), IPS, Intel Celeron J4125, ядра: 4 х 2 ГГц, RAM 8 ГБ, SSD 240 ГБ, Intel UHD Graphics 600 , Windows 10 Pro',32000,4),
    (6,6,1,6,"Dell Vostro 3400-4579",'14",Full HD (1920x1080), WVA (TN+film), Intel Core i3-1115G4, ядра: 2 х 3 ГГц, RAM 4 ГБ, HDD 1000 ГБ, SSD 256 ГБ, Intel UHD Graphics , Linux',29999,7),
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
# cursor.execute(insert_query[0], categories)
cursor.execute(insert_query[1], imgs)
# cursor.execute(insert_query[2], manufacturers)
cursor.execute(insert_query[3], products)
