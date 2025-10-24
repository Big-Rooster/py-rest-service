# Multi-stage Docker build for PyRest Service
FROM python:3.11-slim as builder

# Set environment variables for Python
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /usr/local/bin/

# Set work directory
WORKDIR /app

# Copy all package configurations
COPY pyproject.toml uv.lock* ./
COPY py-rest-service-core/pyproject.toml ./py-rest-service-core/
COPY py-rest-service-persistence/pyproject.toml ./py-rest-service-persistence/
COPY py-rest-service-api/pyproject.toml ./py-rest-service-api/
COPY py-rest-service-client/pyproject.toml ./py-rest-service-client/
COPY py-rest-service-server/pyproject.toml ./py-rest-service-server/

# Copy all source code
COPY py-rest-service-core/src ./py-rest-service-core/src/
COPY py-rest-service-persistence/src ./py-rest-service-persistence/src/
COPY py-rest-service-api/src ./py-rest-service-api/src/
COPY py-rest-service-client/src ./py-rest-service-client/src/
COPY py-rest-service-server/src ./py-rest-service-server/src/

# Copy scripts
COPY scripts ./scripts

# Install dependencies
RUN uv sync --frozen --no-dev

# Production stage
FROM python:3.11-slim as production

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PATH="/app/.venv/bin:$PATH"

# Install runtime dependencies
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Create non-root user
RUN groupadd -r appuser && useradd -r -g appuser appuser

# Set work directory
WORKDIR /app

# Copy virtual environment and full application from builder stage
COPY --from=builder --chown=appuser:appuser /app /app

# Switch to non-root user
USER appuser

# Set working directory to server package to avoid namespace conflicts
WORKDIR /app/py-rest-service-server/src

# Expose ports (FastAPI default 8000, management 8080)
EXPOSE 8000 8080

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=30s --retries=3 \
    CMD curl -f http://localhost:8080/health/live || exit 1

# Default command  
CMD ["python", "-m", "ybor_technologies.big_rooster.py_rest.service.server.main"]