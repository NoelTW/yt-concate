from .step import Step
from yt_concate.model.yt import YT


class InitailizeYT(Step):
    def process(self, data, inputs, utils):
        return [YT(url) for url in data]
