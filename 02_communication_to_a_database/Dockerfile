# Use an official Python runtime as a parent image
FROM python:3.6-slim

WORKDIR /tmp_install
COPY requirements.txt /tmp_install
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Update repositories
RUN pip install qrcode[pil]

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "app.py"]