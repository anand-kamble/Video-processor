from colorama import Fore, Style
import datetime
import sys


class Logger:
    def __init__(self, scope: str, ):
        self.scope = scope or ""
        self.debugMode = "--debug" in sys.argv
        self.logFileName = "logs.txt"
        pass

    def log(self, msg: str):
        logString: str = '[' + self.scope + '] : ' + msg
        self.__log(
            datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")+" \n\t[LOG] @" + logString)
        print(Fore.BLUE + logString + Style.RESET_ALL) if self.debugMode else 0

    def warn(self, msg: str):
        logString: str = '[' + self.scope + '] : ' + msg
        self.__log(
            datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")+" \n\t[WARN] @" + logString)
        print(Fore.YELLOW + logString + Style.RESET_ALL) if self.debugMode else 0

    def error(self, msg: str):
        logString: str = '[' + self.scope + '] : ' + msg
        self.__log(
            datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")+" \n\t[ERROR] @" + logString)
        print(Fore.RED + logString + Style.RESET_ALL) if self.debugMode else 0

    def __log(self, msg: str):
        try:
            file1 = open(self.logFileName, "a")
            file1.write(msg+'\n')
            file1.close()
            pass
        except Exception as e:
            print(Fore.RED + "Failed to write logs to " +
                  self.logFileName + "\n" + str(e) + Style.RESET_ALL)
            pass
