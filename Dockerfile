# Use an official Python runtime as a base image
FROM python:3.12.6

# Install bash
RUN apt-get update && apt-get install -y bash

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY req.txt /app/
RUN pip install -r req.txt

# Copy the entire project directory into the container
COPY . /app/

# Expose port 8000 for Django
EXPOSE 8000

# Run the Django development server
CMD ["python", "ibot_lms/manage.py", "runserver", "0.0.0.0:8000"]
