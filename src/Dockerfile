# Use the official Python image as the base image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the Python application code into the container
COPY display.py /app/

# Install Flask and other dependencies
RUN pip install flask

# Run the Python application when the container starts
CMD ["python", "display.py"]
