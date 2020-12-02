FROM python:3

RUN mkdir /app
WORKDIR /app
ADD requirements.txt /app/requirements.txt
RUN pip3 install -r requirements.txt

COPY . /app/

CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8013" ]
