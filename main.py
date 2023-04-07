from Class.VIDEO_SUBTITLE_MAKER import VIDEO_SUBTITLE_MAKER

# "C:/Users/91911/Documents/JDownloader/Miley Cyrus - Flowers (Official Video) (1406p_24fps_AV1-128kbit_AAC).mp4"


def main():
    VIDEO_SUBTITLE_MKR = VIDEO_SUBTITLE_MAKER()
    video_path = input("Enter the path to your video: \n")
    if (VIDEO_SUBTITLE_MKR.add_video(video_path=video_path)):
        VIDEO_SUBTITLE_MKR.prepare()
    else:
        print("Failed to load video. Please check the path you entered")
        VIDEO_SUBTITLE_MKR.destoy()
        main()


main()
