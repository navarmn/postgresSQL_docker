Using a container with an external database
======

Before start this example we assume you have completed the step [01_container_with_postgres](../01_container_with_postgres) to have a postgres database running on you machine within a container.

There two you ways you can accomplish this. However thinking in a rea word application, we assume your container wants to communicate with a external database running anywhere with and internet connection. For more details see this discussion at [https://stackoverflow.com/questions/48051970/unable-to-connect-outside-database-from-docker-container-app](https://stackoverflow.com/questions/48051970/unable-to-connect-outside-database-from-docker-container-app)


## Build the container and run it

This is pretty straightfoward as:

``` shell
docker build -t app_to_db .
```

The trick here is to set the container to use the machine IP by passing during ```run``` command:

``` shell
docker run -d --net host app_to_db 
```

or, use ```docker-compose up``` that everything goes up with a single shot :). See how beautiful is docker?!

And, done! Your applications is up and running. You can use ```docker ps``` and ```docker-compose ps``` on terminal to see this container.

### What does the app do?

It is a dumb app. It just reads the database each 10 seconds, look for new entries, generate a QR-code using a #hash key and stores on you local folder under *qr_images*. See the ```.yml``` file for details.




