FROM python:3.6

RUN apt-get update

ENV PYTHONBUFFERED=1
ENV STATIC_ROOT=/usr/src/app/static

EXPOSE 8000
WORKDIR /usr/src/app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN pip install pillow

COPY . /usr/src/app

CMD ["./Scripts/run_django.sh"]

# create unprivileged user
RUN adduser --disabled-password --gecos '' myuser  



