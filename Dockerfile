# Use an official Python runtime as a base image
FROM python:3.12.6

# Install bash and any additional dependencies
RUN apt-get update && apt-get install -y bash && rm -rf /var/lib/apt/lists/*

# Set the working directory inside the container
WORKDIR /app

RUN pip install -r /app/req.txt
RUN chmod 666 /app/ibot_lms/requests.log

# Copy the entire project directory into the container
COPY . .

# Expose port 8000 for Django
EXPOSE 8000

# Run the Django development server
CMD ["python", "ibot_lms/manage.py", "runserver", "0.0.0.0:8000"]
