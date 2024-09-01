from io import BytesIO

from django.core.files.base import ContentFile
from PIL import Image


def resize_image(image, file_name: str, max_width=None, max_height=None):
    img = image.copy()

    original_width, original_height = img.size

    if max_width and max_height:
        scale_factor = min(max_width / original_width, max_height / original_height)
    elif max_width:
        scale_factor = max_width / original_width
    elif max_height:
        scale_factor = max_height / original_height
    else:
        scale_factor = 1

    new_size = (int(original_width * scale_factor), int(original_height * scale_factor))

    # Use a high-quality resampling filter
    img = img.resize(new_size, Image.LANCZOS)

    thumb_io = BytesIO()

    # Save the image with high quality
    img_format = image.format if image.format else 'JPEG'
    if img_format == 'JPEG':
        img.save(thumb_io, format=img_format, quality=95)  # Set quality to 95%
    else:
        img.save(thumb_io, format=img_format)

    thumbnail = ContentFile(thumb_io.getvalue(), name=file_name)

    return thumbnail
