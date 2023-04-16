import ffmpeg
from Class.Logger import Logger
from Class.GLOBAL_VARIABLES import VIDEO_PROCESSOR_GLOBAL_VARIABLES_CLASS
from Constants import TEMP_DIR_NAME, TEMP_AUDIO_FILE_NAME, VIDEO_PATH_KEY


class FFMPEG_HANDLER:
    def __init__(self, global_variables: VIDEO_PROCESSOR_GLOBAL_VARIABLES_CLASS):
        self.path = ""
        self.GLOBAL_VARIABLES = global_variables
        self.Logger = Logger("FFMPEG_HANDLER")
        return None

    def update_path(self, path: str):
        try:
            self.path = str(path)
            return self
        except:
            self.Logger.warn("Failed to update path, trying again ...")
            self.update_path(str(path))

    def extract_audio(self):
        try:
            (ffmpeg
             .input(self.GLOBAL_VARIABLES.use(VIDEO_PATH_KEY))
                .output(TEMP_DIR_NAME+'/'+TEMP_AUDIO_FILE_NAME, q=0, map="a", loglevel="quiet")
                .run_async(pipe_stdout=True)
             )
        except Exception as e:
            self.Logger.error("Failed to add video path\n\t"+str(e))
            pass
