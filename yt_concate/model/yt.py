import os

from yt_concate.settings import CAPTION_DIR
from yt_concate.settings import VIDEO_DIR


class YT:
    def __init__(self, url):
        self.url = url
        self.id = self.get_video_id()
        self.captions_dir = self.get_captions_dir()
        self.captions = None

    def __str__(self):
        return f'<{self.id} exist>'

    def __repr__(self):
        return ':'.join({self.id}, self.captions_dir, self.captions)

    def get_video_id(self):
        return self.url.split('watch?v=')[-1]

    def get_captions_dir(self):
        return os.path.join(CAPTION_DIR, self.id + '.txt')

    def get_video_dir(self):
        return os.path.join(VIDEO_DIR, self.id + '.txt')
