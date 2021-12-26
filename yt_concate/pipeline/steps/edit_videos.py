from moviepy.editor import VideoFileClip
from moviepy.editor import concatenate_videoclips

from .step import Step


class EditVideos(Step):
    def process(self, data, inputs, utils):
        clips = []
        for found in data:
            start = found.time['start']
            end = found.time['start'] + found.time['duration'] + 1.5
            video = VideoFileClip(found.yt.videos_dir).subclip(start, end)
            clips.append(video)
            if len(clips) == inputs['limit']:
                break
        final_clip = concatenate_videoclips(clips)
        final_clip_name = utils.output_file_dir(inputs['channel_id'], inputs['keywords'])
        print(final_clip_name)
        final_clip.write_videofile(final_clip_name)
