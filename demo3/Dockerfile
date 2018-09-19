FROM python:2.7.15-alpine3.6
COPY server.py ./
COPY requirements.txt ./
RUN pip install -r requirements.txt
EXPOSE 8000
CMD python server.py
