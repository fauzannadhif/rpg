# Use an official Python runtime as a parent image
FROM python:3.8.2-alpine

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apk update && \
    apk add --no-cache \
    gcc \
    musl-dev \
    libffi-dev \
    openssl-dev \
    python3-dev \
    && rm -rf /var/cache/apk/*

# Upgrade pip to the latest version
RUN pip install --no-cache-dir --upgrade pip

# Copy the current directory contents into the container at /app
COPY . /app

COPY ../requirements.txt /app

# Install any dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 7000 available to the world outside this container
EXPOSE 7000