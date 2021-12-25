from pytube import YouTube

from yt_concate.settings import VIDEO_DIR
from .step import Step


class DownloadVideos(Step):
    def process(self, data, inputs, utils):
        print('before set :', len(data))
        set_yt = set([found.yt for found in data])
        print('after set :', len(set_yt))
        for yt in set_yt:
            if yt.videos_dir:
                print('Video > ', yt.videos_dir, 'exists... skipping')
                continue
            url = yt.url
            id_ = yt.id
            print(f'downloading {url}')
            YouTube(url).streams.get_highest_resolution().download(output_path=VIDEO_DIR, filename=id_ + '.mp4')
        return data
