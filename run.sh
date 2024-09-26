#!/bin/sh

python manage.py migrate
python manage.py createsuperuser --noinput
python manage.py collectstatic --noinput

unlink /etc/nginx/sites-enabled/default
nginx -g 'daemon off;' &

sleep 5

# Check if SSL certificates exist in S3
if aws s3 ls s3://django-portfolio-assets/ssl-certs/fullchain.pem > /dev/null 2>&1; then
  mkdir -p /etc/letsencrypt/live/samdolat.com
  echo "SSL certificates found on S3. Downloading..."
  aws s3 cp s3://django-portfolio-assets/ssl-certs/fullchain.pem /etc/letsencrypt/live/samdolat.com/fullchain.pem
  aws s3 cp s3://django-portfolio-assets/ssl-certs/privkey.pem /etc/letsencrypt/live/samdolat.com/privkey.pem
  chmod 600 /etc/letsencrypt/live/samdolat.com/privkey.pem
  chmod 600 /etc/letsencrypt/live/samdolat.com/fullchain.pem
else
  cp ./configs/nginx/nginx.http.conf /etc/nginx/conf.d/default.conf
  nginx -s reload

  echo "SSL certificates not found. Generating new ones with Certbot..."
  certbot certonly --webroot --webroot-path=/var/www/certbot --email $DJANGO_SUPERUSER_EMAIL --agree-tos --no-eff-email -d samdolat.com -d www.samdolat.com

  # Upload new certificates to S3
  aws s3 cp /etc/letsencrypt/live/samdolat.com/fullchain.pem s3://django-portfolio-assets/ssl-certs/
  aws s3 cp /etc/letsencrypt/live/samdolat.com/privkey.pem s3://django-portfolio-assets/ssl-certs/
fi

cp ./configs/nginx/nginx.https.conf /etc/nginx/conf.d/default.conf

nginx -t
nginx -s reload

gunicorn -c ./configs/gunicorn/gunicorn.conf.py
