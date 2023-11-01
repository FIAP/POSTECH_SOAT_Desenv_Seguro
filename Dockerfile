FROM python:3.9.12-slim

RUN apt-get update -y && \ 
    apt-get install gcc -y && \
    apt-get install tk -y

WORKDIR /opt

ADD requirements.txt /opt
RUN pip install -r requirements.txt

ADD /src/app /opt/
RUN ls -lh /opt

EXPOSE 5000

CMD ["python","app.py"]