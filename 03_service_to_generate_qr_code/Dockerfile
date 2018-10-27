# Use an official Python runtime as a parent image
FROM "ubuntu"

# Update repositories
RUN apt-get -y update | apt-get upgrade -y

# Install postgres
RUN apt-get -y install postgresql postgresql-contrib
RUN apt-get install postgresql-10

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
# RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME World

# Run app.py when the container launches
# CMD ["python", "app.py"]