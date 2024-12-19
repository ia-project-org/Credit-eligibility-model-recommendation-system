# Stage 1: Build stage using a fully featured Python image
FROM python:3.11-slim AS base

# Expose the port
EXPOSE 8000

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install system dependencies required for Python packages
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    --no-install-recommends && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory for the application
WORKDIR /app

# Copy only the requirements.txt first to take advantage of Docker's caching
COPY requirements.txt /app/

# Upgrade pip and install the Python dependencies
RUN python -m pip install --upgrade pip && \
    python -m pip install -r /app/requirements.txt

# Stage 2: Runtime stage using the distroless image
# FROM gcr.io/distroless/python3-debian12 AS runtime-stage
FROM python:3.11-slim

# Set the working directory in the runtime container
WORKDIR /app

COPY --from=base /usr/local /usr/local
COPY --from=base /app /app

# Copy the application code into the container
COPY ./src /app
COPY ./src/ml/scaler.pkl /app/ml/scaler.pkl
COPY ./src/ml/100k_ann_model.keras /app/ml/100k_ann_model.keras


# Set the entrypoint to start the Django application
ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]
