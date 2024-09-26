FROM python:3.12

RUN apt-get update && \
    apt-get install -y \
    curl \
    unzip \
    nginx \
    certbot \
    python3-certbot-nginx && \
    curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" && \
    unzip awscliv2.zip && \
    ./aws/install

RUN mkdir /django_app && cd /django_app

WORKDIR /django_app

COPY ./configs/nginx/nginx.http.conf /etc/nginx/nginx.conf
COPY ./configs/nginx/certbot /var/www/certbot
COPY ./configs/nginx/ssl /etc/letsencrypt

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN chmod +x run.sh

EXPOSE 80 443

CMD ["./run.sh"]