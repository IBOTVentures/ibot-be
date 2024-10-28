# Use an official Python runtime as a parent image
FROM python:3.12

# Set environment variables to prevent Python from writing .pyc files
# and to ensure that the output is sent straight to the terminal
# (for easier debugging).
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create a new user
RUN useradd -m appuser

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Create the log file and set permissions
RUN touch /app/requests.log && \
    chown appuser:appuser /app/requests.log && \
    chmod 664 /app/requests.log

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r req.txt

# Switch to the new user
USER appuser

# Expose the port the app runs on
EXPOSE 8000

# Run the application (replace with your actual command if different)
CMD ["python", "ibot_lms/manage.py", "runserver", "0.0.0.0:8000"]
