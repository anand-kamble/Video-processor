from colorama import Fore, Style
from os.path import exists, isdir
from os import makedirs, getcwd
from sys import exit
from shutil import rmtree
from Class.GLOBAL_VARIABLES import VIDEO_PROCESSOR_GLOBAL_VARIABLES_CLASS
from Class.Ffmpeg import FFMPEG_HANDLER
from Class.Logger import Logger
from Constants import VIDEO_PATH_KEY, TEMP_DIR_NAME


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
                    VIDEO_PATH_KEY, video_path)
                self.Logger.log("Video Path added" + "'" + video_path + "'")
                return True
            else:
                return False
        except Exception as e:
            self.Logger.error("Failed to add video path\n\t"+str(e))
            pass

    def generate_required_files(self):
        self.FFMPEG_HANDLER.update_path(
            self.GLOBAL_VARIABLES.use(VIDEO_PATH_KEY)).extract_audio()
        return self

    def prepare(self):
        try:
            if not isdir(TEMP_DIR_NAME):
                self.__create_temp_dir()
            else:
                self.__remove_temp_dir()
                self.__create_temp_dir()
            return self
        except Exception as e:
            self.Logger.error("Failed to prepare\n\t"+str(e))
            print(
                Fore.RED + "Failed to modify directories. \n[Hint] : Please check permissions given to program to access and modify files on the system and try again." + Style.RESET_ALL)
            exit()
            pass

    def destoy(self):
        self.__remove_temp_dir()
        self.Logger.log("Instance destoyed.")
        del self

    def __create_temp_dir(self):
        makedirs(getcwd() + "/"+TEMP_DIR_NAME)

    def __remove_temp_dir(self):
        try:
            rmtree(getcwd() + "/"+TEMP_DIR_NAME)
        except:
            return None
