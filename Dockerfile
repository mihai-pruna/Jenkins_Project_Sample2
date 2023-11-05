FROM python:3.9.0-alpine

WORKDIR /delft

COPY requirements.txt .
COPY weather_data.py .

RUN apk add libc-dev gcc
RUN pip install -r requirements.txt

CMD [ "python", "-u", "./weather_data.py" ]