FROM python:3.7-alpine
RUN mkdir -p /config
WORKDIR /code
ENV FLASK_APP=proxy_primary.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
RUN pip install flask
RUN pip install python-nginx
EXPOSE 5000
COPY . .
CMD ["flask", "run"]


