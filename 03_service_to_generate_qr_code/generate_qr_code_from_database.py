import psycopg2
import argparse
import os

from DB import *

def main(args):

    sql = "SELECT * FROM {};".format(args['table_name'])

    table = SELECT(sql)

    key = []
    for row in table:
        new_row = [str(i) for i in row]
        key = ('_'.join(new_row))

        if not os.path.exists('qr_images'):
            os.system('mkdir qr_images')

        os.system('qr "{}" > ./qr_images/{}.png'.format(key, key))
        print('QR-code generated with key: {}'.format(key))

    return None
  
if __name__ == '__main__':
  
  # Arguments
  parser = argparse.ArgumentParser(description='QR code generation 0.0.1')
  parser.add_argument('--table-name', default="0", type=str)
  args = vars(parser.parse_args())    
  
  main(args)

# python generate_qr_code_from_database.py --table-name products