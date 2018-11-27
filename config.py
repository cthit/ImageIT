import os

IMAGE_FOLDER = os.environ.get('IMAGEIT_IMAGE_FOLDER', './images')
ALLOWED_EXTENSIONS = {e.strip() for e in os.environ
    .get('IMAGEIT_ALLOWED_EXTENSIONS', "png, jpg, jpeg, gif").split(",")}

POSTGRES_USER = os.environ.get('IMAGEIT_POSTGRES_USER', 'postgres')

POSTGRES_PASSWORD = os.environ.get('IMAGEIT_POSTGRES_PASSWORD', 'password')
POSTGRES_HOST = os.environ.get('IMAGEIT_POSTGRES_HOST', 'localhost')
POSTGRES_DB = os.environ.get('IMAGEIT_POSTGRES_DB', 'postgres')
