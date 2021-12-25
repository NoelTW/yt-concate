from youtube_transcript_api import YouTubeTranscriptApi

from yt_concate.pipeline.steps.step import Step


class DownloadCaptions(Step):
    def process(self, data, inputs, utils):
        for url in data:
            video_id = utils.get_video_id(url)
            if utils.caption_exists(url):
                print(video_id, ' already downloaded')
                continue
            try:
                srt = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])
            except:
                print('KeyError when downloading', url)
                continue

            with open(utils.get_captions_dir(url), 'w', encoding='utf-8') as f:
                for i in srt:
                    f.write("{}\n".format(i))

            f.close()
