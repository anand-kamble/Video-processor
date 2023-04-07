import ffmpeg
from Class.GLOBAL_VARIABLES import VIDEO_PROCESSOR_GLOBAL_VARIABLES_CLASS
from Constants import TEMP_DIR_NAME, TEMP_AUDIO_FILE_NAME, VIDEO_PATH_KEY


class FFMPEG_HANDLER:
    def __init__(self, global_variables: VIDEO_PROCESSOR_GLOBAL_VARIABLES_CLASS):
        self.path = ""
        self.GLOBAL_VARIABLES = global_variables
        return None

    def update_path(self, path: str):
        self.path = path
        return self

    def extract_audio(self):
        (ffmpeg
         .input(self.GLOBAL_VARIABLES.use(VIDEO_PATH_KEY))
            .output(TEMP_DIR_NAME+'/'+TEMP_AUDIO_FILE_NAME, q=0, map="a", loglevel="quiet")
            .run_async(pipe_stdout=True)
         )
