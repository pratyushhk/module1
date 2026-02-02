FROM python:3.14.2-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/

WORKDIR /app

COPY pyproject.toml .python-version uv.lock ./
RUN uv sync --frozen

ENV PATH="/app/.venv/bin:$PATH"

COPY ingestion.py .

ENTRYPOINT ["python", "ingestion.py"]
