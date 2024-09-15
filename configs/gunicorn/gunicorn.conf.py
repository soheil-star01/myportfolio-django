# gunicorn.conf

wsgi_app = "myportfolio.wsgi:application"

loglevel = "debug"

workers = 2

bind = "0.0.0.0:8000"

accesslog = "-"
errorlog = "-"
# accesslog = "/django_app/logs/gunicorn-access.log"
# errorlog = "/django_app/logs/gunicorn-error.log"
