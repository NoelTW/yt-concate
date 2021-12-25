import os
import ast
from pprint import pprint

from yt_concate.pipeline.steps.step import Step
from yt_concate.settings import CAPTION_DIR


class ReadCaption(Step):

    def process(self, data, inputs, utils):
        data = {}
        for caption_file in os.listdir(CAPTION_DIR):
            captions = {}
            with open(os.path.join(CAPTION_DIR, caption_file), 'r', encoding='utf-8') as f:
                for line in f:
                    each_caption = ast.literal_eval(line)
                    captions[each_caption['text']] = each_caption
                    del captions[each_caption['text']]['text']
            data[caption_file] = captions
        pprint(data)
        return data
