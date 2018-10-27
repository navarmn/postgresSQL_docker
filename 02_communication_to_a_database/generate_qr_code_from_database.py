import psycopg2
import argparse
import os
import sys

from DB import INSERT
from DB import SELECT

'''
Script that works as following:
==================================
Given an ID, grab all information in the table, generate a #key, 
creates as QR-code and returns its directory
'''


def main(args):

    print(os.getcwd())

    _hash = 'id, company, city, uf, product_name'
    _id = args['id']

    sql = 'select {} from products where id = {};'.format(_hash, _id)

    table = SELECT(sql)

    key = []
    for row in table:
        new_row = [str(i) for i in row]
        key = ('_'.join(new_row))

        if not os.path.exists('qr_images'):
            os.system('mkdir qr_images')

        os.system('qr "{}" > ./qr_images/{}.png'.format(key, key))
        print('QR-code generated with key: {}'.format(key))

    return True
  
if __name__ == '__main__':
  
  # Arguments
  parser = argparse.ArgumentParser(description='QR code generation 0.0.1')
  parser.add_argument('--table-name', default="0", type=str)
  parser.add_argument('--id', default="0", type=str)
  parser.add_argument('--path', default=".", type=str)
  args = vars(parser.parse_args())    
  
  main(args)

# python generate_qr_code_from_database.py --table-name products --id 1