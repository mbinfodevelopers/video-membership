# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory to /backend
WORKDIR /backend

# Copy the current directory contents into the container at /backend
COPY . /backend

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8000 for the Django app to run on
EXPOSE 8000

# Start the Django app
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
