import psycopg2
import housing_prediction

con = None
cur = None
try:
    #connect to the db
    con = psycopg2.connect(
        host = "localhost",
        dbname = "postgres",
        user = "postgres",
        password = "123456",
        port = 5432
    )

    #cursor (to connect to database)
    cur = con.cursor()

    cur.execute('DROP TABLE IF EXISTS houses')
    create_script = ''' CREATE TABLE IF NOT EXISTS houses (
                        id            int PRIMARY KEY,
                        price         varchar(15) NOT NULL,
                        neighborhood  varchar(50) NOT NULL,
                        city          varchar(50) NOT NULL,
                        bedroom       varchar(10) NOT NULL,
                        bathroom      varchar(10) NOT NULL,
                        size          varchar(10) NOT NULL)
                        '''
    cur.execute(create_script)

    insert_script = 'INSERT INTO houses (id, price, neighborhood, city, bedroom, bathroom, size) VALUES (%s, %s, %s, %s, %s, %s, %s)'
    insert_value = housing_prediction.houseSearch()

    for value in insert_value:
        cur.execute(insert_script, value)
    con.commit()



except Exception as error:
    print(error)
finally:
    if cur != None:
        cur.close()
    if con != None:
        con.close()