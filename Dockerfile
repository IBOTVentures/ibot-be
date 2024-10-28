FROM python:3.12.6

RUN apt-get update && apt-get install -y bash

# Create a new user and set permissions
RUN useradd -m appuser

# Set the working directory
WORKDIR /app

# Copy your application code
COPY . .

# Install your requirements
RUN pip install -r requirements.txt

# Switch to the new user
USER appuser

# Set the default command to run your application (if needed)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
