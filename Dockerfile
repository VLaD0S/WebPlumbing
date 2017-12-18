FROM python:3

RUN apt-get update

ENV PYTHONBUFFERED=1
ENV STATIC_ROOT=/usr/src/app/static

EXPOSE 8000
WORKDIR /usr/src/app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . /usr/src/app

CMD ["./Scripts/run_django.sh"]


