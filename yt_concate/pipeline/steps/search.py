from .step import Step
from yt_concate.model.found import Found


class Search(Step):
    def process(self, data, inputs, utils):
        key_word = inputs['keywords']
        found = []
        for yt in data:
            if not yt.captions:
                continue
            for caption in yt.captions:
                if key_word in caption:
                    time = yt.captions[caption]
                    f = Found(yt.id, caption, time)
                    found.append(f)

        print(found)
        return found

