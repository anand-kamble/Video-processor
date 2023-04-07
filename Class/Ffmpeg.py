import ffmpeg
from .GLOBAL_VARIABLES import VIDEO_PROCESSOR_GLOBAL_VARIABLES_CLASS


class FFMPEG_HANDLER:
    def __init__(self, global_variables: VIDEO_PROCESSOR_GLOBAL_VARIABLES_CLASS):
        self.path = ""
        self.GLOBAL_VARIABLES = global_variables
        return None

    def extract_audio(self):
        (ffmpeg
         .input(self.GLOBAL_VARIABLES.use("VIDEO_PATH"))
            .output('out.mp3', q=0, map="a")
            .run_async(pipe_stdout=True)
         )
