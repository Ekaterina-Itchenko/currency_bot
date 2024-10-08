FROM python:3.11 as requirements_stage

ENV PYTHONUNBUFFERED = 1

WORKDIR /tmp

RUN pip3 install poetry

COPY ./pyproject.toml ./poetry.lock* /tmp/

RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

FROM python:3.11

WORKDIR /project

COPY --from=requirements_stage /tmp/requirements.txt /project/requirements.txt

RUN apt-get update \
  && apt-get install -y build-essential \
  && apt-get install -y gettext \
  && pip install --no-cache-dir --upgrade -r /project/requirements.txt

ENV TELEGRAM_TOKEN ${TELEGRAM_TOKEN}

COPY . /project

CMD ["python3", "src/main.py", "", "0.0.0.0:8000"]