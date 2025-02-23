FROM python:3.12-slim-bookworm
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

RUN addgroup --system appuser && \
    adduser --system --group --home /home/appuser appuser

RUN mkdir /app && \
    chown appuser:appuser /app

WORKDIR /app

USER appuser

ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy

RUN uv venv

COPY --chown=appuser:appuser . /app/

RUN uv sync

ENV PATH="/app/.venv/bin:$PATH"

CMD ["celery", "-A", "murner.tasks", "--workdir", "src/murner", "worker", "--loglevel=info"]
