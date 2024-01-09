FROM python:3.9.18-slim-bullseye 
RUN apt update \
  && apt install libpq-dev gcc -y \
  && pip install flask psycopg2-binary configparser \
  && apt remove gcc -y \
  && apt autoremove -y \
  && apt clean \
  && rm -rf /var/lib/apt/lists/* /var/tmp/* /var/cache/apt/*
ENTRYPOINT /usr/local/bin/python /srv/app/web.py
