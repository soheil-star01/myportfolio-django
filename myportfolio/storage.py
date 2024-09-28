import os
from urllib.parse import urljoin

from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class CkeditorS3BotoStorage(S3Boto3Storage):
    default_acl = 'private'
    file_overwrite = False
    location = os.path.join(settings.MEDIA_ROOT, "ckeditor")
    base_url = urljoin(settings.MEDIA_URL, "ckeditor/")
