# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the files from src to the working directory
COPY . .

# Install Node.js and npm
RUN apt-get update && apt-get install -y nodejs npm

# Install Vue CLI
RUN npm install -g @vue/cli

# Install dependencies for frontend
RUN npm install && npm run build

# Expose port 8000 for the Django app
EXPOSE 8000

# Start the Django app
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
