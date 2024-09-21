#!/bin/sh

python manage.py makemigrations
python manage.py makemigrations blog
python manage.py makemigrations photo_gallery
python manage.py migrate
python manage.py createsuperuser --noinput

python manage.py collectstatic --noinput

unlink /etc/nginx/sites-enabled/default
nginx -g 'daemon off;' &

sleep 5

gunicorn -c ./configs/gunicorn/gunicorn.conf.py

#
#certbot certonly --webroot --webroot-path=/var/www/certbot --email $LETSENCRYPT_EMAIL --agree-tos --no-eff-email -d samdolat.com -d www.samdolat.com
#
#cp /etc/nginx/conf.d/nginx.https.conf /etc/nginx/conf.d/default.conf
#
#nginx -s reload