import os

from yt_concate.pipeline.steps.step import Step


class PreFlight(Step):

    def process(self, data, inputs, utils):
        print('------------in preflight-------------')
        utils.create_dir()
