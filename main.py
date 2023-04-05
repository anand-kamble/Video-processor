from ffmpeg import input, output, run
from Class.CONSTANTS import VIDEO_PROCESSOR_CONSTANTS_CLASS

CONSTANTS = VIDEO_PROCESSOR_CONSTANTS_CLASS()


CONSTANTS.create(
    "VIDEO_PATH", "C:/Users/91911/Documents/JDownloader/Miley Cyrus - Flowers (Official Video) (1406p_24fps_AV1-128kbit_AAC).mp4")

inp = input(CONSTANTS.use("VIDEO_PATH"))
# audio = inp.audio.filter("aecho", 0.8, 0.9, 1000, 0.3)
video = inp.video.hflip()
# out = output(video, 'out.mp4')
run(inp)
