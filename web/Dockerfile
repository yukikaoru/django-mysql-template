FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
RUN mkdir /log
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/

