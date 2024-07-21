# Use the official Python image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy the rest of the project files
COPY . .

# Set environment variables for Django
ENV DJANGO_SETTINGS_MODULE=myproject.settings
ENV PYTHONUNBUFFERED 1

# Collect static files
RUN python manage.py collectstatic --noinput

# Run the development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
