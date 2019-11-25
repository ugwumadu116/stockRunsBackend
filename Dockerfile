FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt


# python manage.py runserver 0.0.0.0:$PORT
