import urllib.request
import json

from yt_concate.pipeline.steps.step import Step
from yt_concate.settings import API_KEY


class GetVideoList(Step):
    def process(self, data, inputs, utils):
        channel_id = inputs["channel_id"]
        if utils.video_list_file_exist(channel_id):
            print('Found existing video list for channel', channel_id)
            return self.read_file(utils.get_video_list_file_path(channel_id))

        api_key = API_KEY
        base_video_url = 'https://www.youtube.com/watch?v='
        base_search_url = 'https://www.googleapis.com/youtube/v3/search?'

        first_url = base_search_url + 'key={}&channelId={}&part=snippet,id&order=date&maxResults=25'.format(api_key,
                                                                                                            channel_id)

        video_links = []
        url = first_url
        while True:
            inp = urllib.request.urlopen(url)
            resp = json.load(inp)

            for i in resp['items']:
                if i['id']['kind'] == "youtube#video":
                    video_links.append(base_video_url + i['id']['videoId'])
            try:
                next_page_token = resp['nextPageToken']
                url = first_url + '&pageToken={}'.format(next_page_token)
            except KeyError:
                break
        print(video_links)
        self.save_video_url_to_file(video_links, utils.get_video_list_file_path(channel_id))
        return video_links

    def save_video_url_to_file(self, video_links, filepath):
        with open(filepath, 'w', encoding='utf-8') as f:
            for url in video_links:
                f.write(url + '\n')

    def read_file(self, filepath):
        video_links = []
        with open(filepath, 'r') as f:
            for line in f:
                video_links.append(line.strip())
        return video_links
