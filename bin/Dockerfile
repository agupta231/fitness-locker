FROM python:3

RUN apt update && apt install -y cron curl
RUN pip install flask



WORKDIR /app
CMD python -u locker.py
