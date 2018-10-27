import psycopg2
import argparse

from DB import *


def main(args):


    sql = """INSERT INTO products (company, city, uf, product_name)
             VALUES (%s, %s, %s, %s) RETURNING id;"""
    
    INSERT(sql, args['company_name'], args['city'], args['uf'], args['product_name']) 

    return None
  
if __name__ == '__main__':
  
  # Arguments
  parser = argparse.ArgumentParser(description='QR code generation 0.0.1')
  parser.add_argument('--company-name', default="0", type=str)
  parser.add_argument('--city', default="0", type=str)
  parser.add_argument('--uf', default="0", type=str)
  parser.add_argument('--product-name', default="0", type=str)
  args = vars(parser.parse_args())    
  
  main(args)

# python insert_products_database.py --company-name Empresa_Pedro --city Fortaleza --uf CE --product-name Cachaça