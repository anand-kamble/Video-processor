from .GLOBAL_VARIABLES import VIDEO_PROCESSOR_GLOBAL_VARIABLES_CLASS
from .Ffmpeg import FFMPEG_HANDLER
from .Logger import Logger
from os.path import exists, isdir


class VIDEO_SUBTITLE_MAKER:
    def __init__(self):
        try:
            self.Logger = Logger("VIDEO_SUBTITLE_MAKER")
            self.GLOBAL_VARIABLES = VIDEO_PROCESSOR_GLOBAL_VARIABLES_CLASS()
            self.FFMPEG_HANDLER = FFMPEG_HANDLER(self.GLOBAL_VARIABLES)
            self.Logger.log("Initialized")
            return None
        except Exception as e:
            Logger("VIDEO_SUBTITLE_MAKER").error(e)
            pass

    def add_video(self, video_path: str):
        try:
            if (exists(video_path)):
                self.GLOBAL_VARIABLES.create(
                    "VIDEO_PATH", video_path)
                self.Logger.log("Video Path added" + "'" + video_path + "'")
                return True
            else:
                return False
        except Exception as e:
            self.Logger.error("Failed to add video path\n"+e)
            pass

    def generate_required_files(self):
        return self

    def prepare(self):
        print(isdir("temp"))

    def destoy(self):
        self.Logger.log("Instance destoyed.")
        del self
