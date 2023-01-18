FROM python:3.9.2

RUN pip3 install -r requirements.txt
WORKDIR /app
COPY . /app

EXPOSE 5000

ENTRYPOINT ["python3"]
CMD ["app.py"]
