FROM python:3.11-slim AS builder

WORKDIR /build
COPY requirements.txt .
RUN pip install \
    --no-cache-dir \
    --prefix=/install \
    -r requirements.txt

FROM python:3.11-slim

RUN groupadd --system app \
    && useradd --system --gid app --create-home app

WORKDIR /hello

COPY --from=builder /install /usr/local
COPY --chown=app:app hello.py .

ENV PYTHONUNBUFFERED=1

USER app

CMD ["python", "hello.py"]
