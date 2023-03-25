# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

ENV PYTHONUNBUFFERED=1

# Set the working directory to /app
WORKDIR /app

COPY ./src ./

# Copy the requirements file into the container
# COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip --no-cache-dir

RUN pip install -r /app/requirements.txt --no-cache-dir

# Copy the files from src to the working directory
COPY . .

# Install Node.js and npm
# RUN apt-get update && apt-get install -y curl && \
#     curl -sL https://deb.nodesource.com/setup_10.x | bash - && \
#     apt-get install -y nodejs

# # Install Vue CLI
# RUN npm install -g @vue/cli

# RUN npm install -g @vue/cli-service-global

# # Install dependencies for frontend
# RUN apt-get update && apt-get install -y \
#     libpng-dev \
#     libjpeg-dev \
#     libgif-dev \
#     && rm -rf /var/lib/apt/lists/*

# Expose port 8000 for the Django app
EXPOSE 9000

# ENV PATH="/app/node_modules/.bin:$PATH"

# Start the Django app
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]