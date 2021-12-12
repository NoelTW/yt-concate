import os

from yt_concate.settings import VIDEO_DIR
from yt_concate.settings import CAPTION_DIR
from yt_concate.settings import DOWNLOAD_DIR


class Utils:

    def __init__(self):
        pass

    @staticmethod
    def get_video_id(url):
        video_id = url.split('watch?v=')[-1]
        return video_id

    def get_captions_dir(self, url):
        return os.path.join(CAPTION_DIR, self.get_video_id(url) + '.txt')

    @staticmethod
    def create_dir():
        os.makedirs(DOWNLOAD_DIR, exist_ok=True)
        os.makedirs(CAPTION_DIR, exist_ok=True)
        os.makedirs(VIDEO_DIR, exist_ok=True)
