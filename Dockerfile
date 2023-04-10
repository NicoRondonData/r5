FROM python:3.10-alpine

WORKDIR /code

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requierements.txt /code/requierements.txt

RUN apk add build-base
RUN apk add postgresql-libs && \
  apk add --no-cache gcc musl-dev postgresql-dev && \
  pip install -r /code/requierements.txt && \
  rm -rf /var/cache/apk/*



COPY ./app /code/app


CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8042", "--reload"]
