import pandas as pd
import os
import subprocess

from DB import INSERT
from DB import SELECT
from DB import UPDATE

def scan_database():
    
    sql = "SELECT * FROM products;"
    df_columns = ['id', 'company', 'city', 'uf', 'product_name', 'qr_code_dir']
    products_table = pd.DataFrame(SELECT(sql), columns=df_columns)

    sql =   '''
            select column_name 
            from information_schema.columns 
            where table_name = 'products';
            '''
    fieldnames = SELECT(sql)

    # Get a dataframe withou None values
    products_without_qr_code = products_table[products_table['qr_code_dir'].apply(lambda x: x is None)]

    # Iterate over all elements in the table
    for _, product in products_table.iterrows():
        # Double check if there is an qr_code already generated
        if product[-1] == None:
            id_product = product['id']
            # Generate qr code
            print(os.getcwd())
            os.system('python generate_qr_code_from_database.py --table-name products --id {}'.format(id_product))
            # Insert its cornfirmation directory into the database
            sql = "update products set qr_code_dir = True where id = {};".format(id_product)
            print('Value inserted into the database')
            
            UPDATE(sql)

    return True


