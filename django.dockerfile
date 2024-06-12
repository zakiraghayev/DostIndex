# Use the official Python image as the base image
FROM python:3.12

# Set an environment variable to ensure Python output is sent straight to the terminal without being buffered
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /usr/src/app

# Install gettext for message translation
RUN apt-get update && apt-get install -y gettext

# Copy only the requirements file, to cache the installed dependencies
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code to the container
COPY . .

# Create a non-root user and switch to it
RUN adduser --disabled-password --gecos '' nonrootuser

USER nonrootuser
