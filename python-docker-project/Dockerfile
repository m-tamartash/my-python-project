# استفاده از image پایه پایتون ۳.۱۲.۳
FROM python:3.12.3-slim

# Set the working directory in the container
WORKDIR /app

# Copy the project files into the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the new port
EXPOSE 5002

# Command to run the application
CMD ["python", "app.py"]
