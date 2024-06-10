# Use the official Python image from the Docker Hub
FROM python:3.10

# Set environment variables to prevent Python from writing .pyc files to disk
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install any dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app/

# Copy the .env file into the container
COPY library.env /app/library.env

# Copy entrypoint.sh
COPY ./entrypoint.sh /app/entrypoint.sh

# Make entrypoint.sh executable
RUN chmod +x /app/entrypoint.sh

# Expose the port the app runs on
EXPOSE 8000

# Define the entrypoint script
ENTRYPOINT ["/app/entrypoint.sh"]

# Define the command to run the application
CMD ["gunicorn", "--workers", "3", "config.wsgi:application", "--bind", "0.0.0.0:8000"]
