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

# Install supervisor
RUN pip install supervisor

# Copy the current directory contents into the container at /app
COPY . /app

# Configure supervisord
COPY supervisord.conf /etc/supervisord.conf

# Install any dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 9000 available to the world outside this container
EXPOSE 9000

# Start supervisord
CMD ["supervisord", "-c", "/etc/supervisord.conf"]