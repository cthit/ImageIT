import os

IMAGE_FOLDER = os.environ.get('IMAGEIT_IMAGE_FOLDER', 'C:/ImageIT/images')
ALLOWED_EXTENSIONS = {e.strip() for e in os.environ
    .get('IMAGEIT_ALLOWED_EXTENSIONS', "png, jpg, jpeg, gif").split(",")}
