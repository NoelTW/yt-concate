from youtube_transcript_api import YouTubeTranscriptApi

from yt_concate.pipeline.steps.step import Step


class DownloadCaptions(Step):
    def process(self, data, inputs, utils):
        for yt in data:
            url = yt.url
            video_id = yt.id
            captions_dir = yt.captions_dir
            if utils.caption_exists(yt):
                print(video_id, 'captions already downloaded')
                continue
            try:
                srt = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])
            except:
                print('KeyError when downloading', url)
                continue

            with open(captions_dir, 'w', encoding='utf-8') as f:
                for i in srt:
                    f.write("{}\n".format(i))
            f.close()
        return data
