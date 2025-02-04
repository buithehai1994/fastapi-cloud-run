# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt into the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the FastAPI app into the container
COPY . /app

# Expose port 8000
EXPOSE 8000

# Run the FastAPI app with Uvicorn (ASGI server)
CMD ["uvicorn", "backend.api:app", "--host", "0.0.0.0", "--port", "8000"]
