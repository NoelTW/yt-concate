from yt_concate.utils import Utils
from yt_concate.pipeline.pipeline import Pipeline
from yt_concate.pipeline.steps.preflight import PreFlight
from yt_concate.pipeline.steps.get_video_list import GetVideoList
from yt_concate.pipeline.steps.initialize import InitailizeYT
from yt_concate.pipeline.steps.download_caption import DownloadCaptions
from yt_concate.pipeline.steps.read_caption import ReadCaption
from yt_concate.pipeline.steps.search import Search
from yt_concate.pipeline.steps.download_videos import DownloadVideos
from yt_concate.pipeline.steps.postflight import PostFlight

CHANNEL_ID = "UCTnK3UFznEB5bd4vDEFMM4A"


def main():
    steps = [
        PreFlight(),
        GetVideoList(),
        InitailizeYT(),
        DownloadCaptions(),
        ReadCaption(),
        Search(),
        DownloadVideos(),
        PostFlight(),
    ]

    inputs = {
        'channel_id': CHANNEL_ID,
        'keywords': 'fantastic',
    }

    utils = Utils()
    p = Pipeline(steps)
    p.run(inputs, utils)


if __name__ == "__main__":
    main()
