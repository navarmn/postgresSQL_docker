CREATE TABLE products (
    id SERIAL PRIMARY KEY, 
    company VARCHAR(50),
    city VARCHAR(50), 
    uf VARCHAR(2),
    product_name VARCHAR(50),
    qr_code_dir VARCHAR(50)
    );


INSERT INTO products (company, city, uf, product_name)
VALUES ('Empresa_Pedro', 'Fortaleza', 'CE', 'Cachaça') RETURNING id;

INSERT INTO products (company, city, uf, product_name)
VALUES ('Empresa_Navar', 'Fortaleza', 'CE', 'Whey') RETURNING id;

INSERT INTO products (company, city, uf, product_name)
VALUES ('Empresa_Raul', 'Fortaleza', 'CE', 'Pipoca') RETURNING id;
