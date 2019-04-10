FROM python:3

RUN apt update && apt install -y cron curl
RUN pip install flask

ADD crontab /etc/cron.d/fitness_reset_cron

RUN crontab /etc/cron.d/fitness_reset_cron && \
    chmod 0644 /etc/cron.d/fitness_reset_cron && \
		crontab /etc/cron.d/fitness_reset_cron && \
		touch /var/log/cron.log


WORKDIR /app
CMD python -u locker.py
