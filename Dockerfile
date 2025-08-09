# --- Build Stage ---
FROM python:3.12-slim-bookworm AS builder

WORKDIR /usr/src/app

# Install system dependencies required for building wheels or for nmap
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    nmap \
    && rm -rf /var/lib/apt/lists/*

# Install build tools
RUN pip install --upgrade pip wheel setuptools

# Copy the project definition and the source code
COPY pyproject.toml ./
COPY app ./app

# Build the wheels from pyproject.toml
# The '.' tells pip to build the project in the current directory
RUN pip wheel --no-cache-dir --wheel-dir /usr/src/app/wheels .


# --- Final Stage ---
FROM python:3.12-slim-bookworm

WORKDIR /usr/src/app

# Install nmap which is required by the application at runtime
RUN apt-get update && apt-get install -y --no-install-recommends \
    nmap \
    && rm -rf /var/lib/apt/lists/*

# Copy the pre-built wheels from the builder stage
COPY --from=builder /usr/src/app/wheels /wheels

# Install the dependencies from the wheels
RUN pip install --no-cache /wheels/*

# Copy the application code (this will be overwritten by the volume in dev mode,
# but is necessary for a standalone production build)
COPY ./app ./app

# Expose the port the app runs on
EXPOSE 5004

# Define the command to run the application
# We use gunicorn for a more robust server, but flask run is fine for dev
CMD ["flask", "run", "--host=0.0.0.0", "--port=5004"]