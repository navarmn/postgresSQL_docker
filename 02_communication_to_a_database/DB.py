import psycopg2
from config import config

def INSERT(sql, *args):
    """ INSERT method for sql """
    connection = None
    try:
        # connect to the PostgreSQL database
        params = config()
        connection = psycopg2.connect(**params)
        # create a new cursor
        cursor = connection.cursor()
        # execute the INSERT statement
        cursor.execute(sql, args)
        # get the output, if any
        output = cursor.fetchone()
        # commit the changes to the database
        connection.commit()
        # close communication with the database
        cursor.close()
        print("INSERT DONE.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
            print('Database connection closed.')
 
    return output

def SELECT(sql):
    """ SELECT to query data from table """
    connection = None
    try:
        # connect to the PostgreSQL database
        params = config()
        connection = psycopg2.connect(**params)
        # create a new cursor
        cursor = connection.cursor()
        # execute the SELECT statement 
        cursor.execute(sql)
        # get the generated all readings
        output = cursor.fetchall()
        # close communication with the database
        cursor.close()  
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()

    return output

def UPDATE(sql):
    """ UPDATE values in the tables. """

    connection = None
    output = None
    try:
        # connect to the PostgreSQL database
        params = config()
        connection = psycopg2.connect(**params)
        # create a new cursor
        cursor = connection.cursor()
        # execute the SELECT statement 
        cursor.execute(sql)
        # commit the changes to the database
        connection.commit()
        # print(output)
        # close communication with the database
        cursor.close()  
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()

    return output

def QUERY(sql):
    """ General queries that can be written in a single statement. """

    connection = None
    output = None
    try:
        # connect to the PostgreSQL database
        params = config()
        connection = psycopg2.connect(**params)
        # create a new cursor
        cursor = connection.cursor()
        # execute the SELECT statement 
        cursor.execute(sql)
        # get the generated all readings
        output = cursor.fetchone()
        # commit the changes to the database
        connection.commit()
        # print(output)
        # close communication with the database
        cursor.close()  
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()

    return output