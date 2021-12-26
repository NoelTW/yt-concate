import os
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.
API_KEY = os.getenv("API_KEY")

DOWNLOAD_DIR = 'dowloads'
CAPTION_DIR = os.path.join(DOWNLOAD_DIR, 'captions')
VIDEO_DIR = os.path.join(DOWNLOAD_DIR, 'videos')
OUTPUT_DIR = 'output'

