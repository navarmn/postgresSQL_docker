import psycopg2

from DB import *


def main():


    sql = """SELECT * FROM products"""
    
    print(SELECT(sql))

    return None
  
if __name__ == '__main__':
    
  main()

# python select_products_database.py