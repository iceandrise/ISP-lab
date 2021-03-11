FROM python:latest

COPY ./requirements.txt ./lab1/app/
WORKDIR /lab1/app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /lab1/app/

CMD ["python","lab1.py"]
