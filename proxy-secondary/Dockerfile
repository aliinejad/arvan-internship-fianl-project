FROM python:3 
RUN apt update 
RUN apt-get install -y  nginx 
RUN pip3 install inotify
COPY ./req/nginx.conf /etc/nginx/
RUN mkdir -p /etc/nginx/stream
WORKDIR /code
COPY ./reload.py .
COPY ./req/script.sh .
RUN chmod +x script.sh
ENTRYPOINT ./script.sh 





