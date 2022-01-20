FROM python:3.9.6-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /home/app

ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

COPY . $APP_HOME

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev jpeg-dev zlib-dev
RUN pip install --upgrade --no-cache pip
RUN pip install --no-cache-dir -r $APP_HOME/requirements.txt


# copy entrypoint.sh
COPY ./entrypoint.sh .
RUN chmod +x ./entrypoint.sh

# copy project
COPY . .

# run entrypoint.sh
ENTRYPOINT ["/home/app/web/entrypoint.sh"]
