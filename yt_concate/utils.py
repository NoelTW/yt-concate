import os

from yt_concate.settings import VIDEO_DIR
from yt_concate.settings import CAPTION_DIR
from yt_concate.settings import DOWNLOAD_DIR
from yt_concate.settings import OUTPUT_DIR


class Utils:

    def __init__(self):
        pass

    def get_video_list_file_path(self, chennal_id):
        return os.path.join(DOWNLOAD_DIR, chennal_id + '.txt')

    def video_list_file_exist(self, chennal_id):
        dir_ = self.get_video_list_file_path(chennal_id)
        return os.path.exists(dir_) and os.path.getsize(dir_) > 0

    @staticmethod
    def create_dir():
        os.makedirs(DOWNLOAD_DIR, exist_ok=True)
        os.makedirs(CAPTION_DIR, exist_ok=True)
        os.makedirs(VIDEO_DIR, exist_ok=True)
        os.makedirs(OUTPUT_DIR, exist_ok=True)

    @staticmethod
    def caption_exists(yt):
        dir = yt.captions_dir
        return os.path.exists(dir) and os.path.getsize(dir) > 0

    @staticmethod
    def output_file_dir(id_, keywords):
        file_name = id_ + '_' + keywords + '.mp4'
        return os.path.join(OUTPUT_DIR, file_name)
