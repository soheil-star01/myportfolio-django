FROM python:3.12

RUN apt update && apt install -y nginx certbot python3-certbot-nginx

RUN mkdir /django_app && cd /django_app

WORKDIR /django_app

COPY ./configs/nginx/nginx.http.conf /etc/nginx/nginx.conf

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN chmod +x run.sh

EXPOSE 80 443

CMD ["./run.sh"]