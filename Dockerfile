FROM python:3.12-slim

# Prevent Python from buffering stdout/stderr
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install uv for fast dependency resolution
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

# Copy dependency files first for layer caching
COPY pyproject.toml uv.lock ./

# Install dependencies (no dev, system python)
RUN uv sync --frozen --no-dev --no-install-project

# Copy the rest of the application
COPY . .

# Cloud Run injects PORT env var (default 8080)
ENV PORT=8080
EXPOSE 8080

CMD ["uv", "run", "python", "main.py"]
