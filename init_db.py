import psycopg2

conn = None
try:
    conn = psycopg2.connect(user='postgres', password='123456', host='127.0.0.1', port='5432', database='cheemstore')
except (Exception, psycopg2.Error) as e:
    print(e)
print("Database opened successfully")
#-------------------------------------------
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS PRODUCTS;")
cur.execute("DROP TABLE IF EXISTS PRODUCT_CATEGORIES;")
cur.execute(
    '''CREATE TABLE PRODUCT_CATEGORIES
    (
      ID INT PRIMARY KEY     NOT NULL,
      NAME           TEXT    NOT NULL
    );
    '''
)

print("PRODUCT_CATEGORIES table created successfully")

conn.commit()
#--------------
cur = conn.cursor()

cur.execute("INSERT INTO PRODUCT_CATEGORIES (ID,NAME) VALUES (1, 'Máy tính bàn')");
cur.execute("INSERT INTO PRODUCT_CATEGORIES (ID,NAME) VALUES (2, 'Điện thoại')");
cur.execute("INSERT INTO PRODUCT_CATEGORIES (ID,NAME) VALUES (3, 'Máy tính bảng')");
cur.execute("INSERT INTO PRODUCT_CATEGORIES (ID,NAME) VALUES (4, 'Lap top')");


conn.commit()
print("Product category's record inserted successfully")


#-------------------------------------------
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS PRODUCT;")
cur.execute(
    '''CREATE TABLE PRODUCTS
    (
      ID INT PRIMARY    KEY     NOT NULL,
      NAME              TEXT    NOT NULL,
      AMOUNT            INT,
      PRODUCT_CATEGORY  INT,
      FOREIGN KEY (PRODUCT_CATEGORY)
        REFERENCES PRODUCT_CATEGORIES (ID)

    );
    '''
)

print("PRODUCTS table created successfully")

conn.commit()
#--------------
cur = conn.cursor()

cur.execute("INSERT INTO PRODUCTS (ID,NAME,PRODUCT_CATEGORY) VALUES (1, 'Điện thoại Nokia', 2)");
cur.execute("INSERT INTO PRODUCTS (ID,NAME, PRODUCT_CATEGORY) VALUES (2, 'Điện thoại SamSung', 2)");
cur.execute("INSERT INTO PRODUCTS (ID,NAME, PRODUCT_CATEGORY) VALUES (3, 'Laptop Asus VivoBook', 4)");
cur.execute("INSERT INTO PRODUCTS (ID,NAME, PRODUCT_CATEGORY) VALUES (4, 'Lenovo Tab M8', 3)");


conn.commit()
print("Product's record inserted successfully")

conn.close()