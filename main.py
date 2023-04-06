import ffmpeg
from Class.CONSTANTS import VIDEO_PROCESSOR_CONSTANTS_CLASS

CONSTANTS = VIDEO_PROCESSOR_CONSTANTS_CLASS()


CONSTANTS.create(
    "VIDEO_PATH", "C:/Users/91911/Documents/JDownloader/Miley Cyrus - Flowers (Official Video) (1406p_24fps_AV1-128kbit_AAC).mp4")

CONSTANTS.addListener("VIDEO_PATH", "new", lambda x: x**2)
(
    ffmpeg
    .input(CONSTANTS.use("VIDEO_PATH"))
    .hflip()
    .output('output.mp4')
    .run()
)
