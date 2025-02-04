# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt from the root directory into the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the backend code into the container
COPY app/backend /app/backend

# Expose port 8000 (FastAPI default port)
EXPOSE 8000

# Run the FastAPI app with Uvicorn (ASGI server)
CMD ["uvicorn", "backend.api:app", "--host", "0.0.0.0", "--port", "8000"]
