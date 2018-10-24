
This part explains how to create a **container** with PostgreSQL version 10 to communicate your application with it.

>Note: the container image used is the lightweight ```postgres:10-alpine```

## Create the container

Create a container with the PostgreSQL version 10 and expose port 6969 to it.

``` shell
docker pull postgres:10-alpine
docker run --name postgres_db -e POSTGRES_PASSWORD=bjjarmbar -p 6969:5432 -d postgres:10-alpine
psql -h localhost -p 6969 -U postgres
```

Or, thinking about scalability, you can bring up the service using the ```docker-compose.yml``` by doing:

``` shell
docker-compose up 
psql -h localhost -p 6969 -U postgres
```

You can also use the ```-d``` parameter in docker-compose to make it work in detached mode.

See full configuration for using PostgreSQL and Docker in [here](https://docs.docker.com/samples/library/postgres/#connect-to-it-from-an-application)


### Create the data base and the table

By running `psql -h localhost -p 6969 -U postgres` you can see we are able to communicate with the container. And from whiting it do it:

``` sql
create database test_db;
\i create_table.sql
```

Use ```\dt``` or ```SELECT * FROM products;``` to see if it works.

The table ```produts``` contains the following structure

 id |    company    |   city    | uf | product_name 
----|---------------|-----------|----|---------------
  1 | Empresa_Pedro | Fortaleza | CE | Cachaça
  2 | Empresa_Navar | Fortaleza | CE | Whey
  3 | Empresa_Raul  | Fortaleza | CE | Pipoca


### Test the database making INSERT and SELECT METHODS

Install python dependecies with ```pip install -r requirements.txt``` or use a virtual enviroment.

> Before running the scripts bellow you first you need to configurate the ```database.ini``` file with the host, port, database, user and password.

To INSERT do:

``` shell
python insert_products_database.py --company-name Empresa_Pedro --city Fortaleza --uf CE --product-name Cachaça
```

To SELECT do:

``` shell
python select_products_database.py
```





