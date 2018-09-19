FROM python:2.7.15-alpine3.6
COPY server.py ./
COPY requirements.txt ./
RUN pip install -r requirements.txt
EXPOSE 5000
ENV FLASK_APP=server.py
CMD flask run --host=0.0.0.0
