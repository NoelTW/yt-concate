import ast

from yt_concate.pipeline.steps.step import Step
from yt_concate.utils import Utils


class ReadCaption(Step):

    def process(self, data, inputs, utils):
        for yt in data:
            if not Utils.caption_exists(yt):
                continue
            captions = {}
            with open(yt.captions_dir, 'r', encoding='utf-8') as f:
                for line in f:
                    each_caption = ast.literal_eval(line)
                    captions[each_caption['text']] = each_caption
                    del captions[each_caption['text']]['text']
            yt.captions = captions
        return data




