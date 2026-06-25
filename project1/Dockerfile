FROM python:3.15-rc-trixie

WORKDIR /app

COPY flask-app.py requirements.txt /app/

RUN pip install -r requirements.txt

CMD ["python", "flask-app.py"]
