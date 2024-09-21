# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the Django project code to the working directory
COPY . /app/

# Expose the port on which the app will run
EXPOSE 8000

# Collect static files
RUN python manage.py collectstatic --noinput

# Run database migrations
RUN python manage.py migrate --noinput

# Start the Gunicorn server
CMD ["gunicorn", "--workers", "3", "--bind", "0.0.0.0:8000", "your_project_name.wsgi:application"]
