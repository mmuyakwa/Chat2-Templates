# --- Build Stage ---
FROM python:3.12-slim-bookworm AS builder

# Set working directory
WORKDIR /usr/src/app

# Install system dependencies required for building wheels or for nmap
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    nmap \
    && rm -rf /var/lib/apt/lists/*

# Install poetry for dependency management (optional but good practice)
# Or just use pip with a virtual environment
RUN pip install --upgrade pip
COPY requirements.txt ./
RUN pip wheel --no-cache-dir --wheel-dir /usr/src/app/wheels -r requirements.txt


# --- Final Stage ---
FROM python:3.12-slim-bookworm

# Set working directory
WORKDIR /usr/src/app

# Install nmap which is required by the application
RUN apt-get update && apt-get install -y --no-install-recommends \
    nmap \
    && rm -rf /var/lib/apt/lists/*

# Copy the wheels from the builder stage
COPY --from=builder /usr/src/app/wheels /wheels

# Install the dependencies from the wheels
RUN pip install --no-cache /wheels/*

# Copy the application code
COPY ./app ./app

# Expose the port the app runs on
EXPOSE 5000

# Define the command to run the application
CMD ["python", "app/app.py"]
