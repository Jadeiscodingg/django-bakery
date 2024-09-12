# Use the official Python image from the Docker Hub
FROM python:3.10-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt requirements.txt

# Install system dependencies and update SQLite

RUN apt-get update && apt-get install -y \

wget \

build-essential \

libsqlite3-dev \
   
&& wget https://www.sqlite.org/2023/sqlite-autoconf-3420000.tar.gz \
    
&& tar -xvf sqlite-autoconf-3420000.tar.gz \
    
&& cd sqlite-autoconf-3420000 \
    
&& ./configure \
    
&& make \
    
&& make install \
    
&& ldconfig \
    
&& cd .. \
    
&& rm -rf sqlite-autoconf-3420000.tar.gz sqlite-autoconf-3420000

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the rest of your application code into the container
COPY . .

# Expose the port Django will run on
EXPOSE 8000

# Run the Django development server when the container launches
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
