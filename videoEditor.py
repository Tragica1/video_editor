from moviepy.editor import VideoFileClip, concatenate_videoclips, TextClip, CompositeVideoClip


class VideoEdit:
    def __init__(self, filename: str):
        self.video = VideoFileClip(filename)
        self.duration = self.video.duration

    def add_text(self, text: str, fontsize: int, color: str, position: tuple, duration: int, start: int,
                 end: int):
        text_clip = (
            TextClip(text, fontsize=fontsize, color=color)
                .set_position(position)
                .set_duration(duration)
        )
        first_part = self.video.subclip(0, start)
        second_part = self.video.subclip(end, self.duration)
        required_part = self.video.subclip(start, end)
        video_with_text = CompositeVideoClip([required_part, text_clip])
        result = concatenate_videoclips([first_part, video_with_text, second_part])
        self.video = result

    def change_resolution(self, type_of_res: int):
        if type_of_res == 1:
            result = self.video.resize(height=1920, width=1080)
        elif type_of_res == 2:
            result = self.video.resize(height=1080, width=1920)
        else:
            result = self.video.resize(height=1080, width=1080)
        self.video = result

    def trim_video(self, start: int, end: int):
        first_part = self.video.subclip(0, start)
        second_part = self.video.subclip(end, self.duration)
        result = concatenate_videoclips([first_part, second_part])
        self.video = result
