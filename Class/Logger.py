from colorama import Fore, Style
import datetime


class Logger:
    def __init__(self, scope: str):
        self.scope = scope or ""
        pass

    def log(self, msg: str):
        logString: str = '[' + self.scope + '] : ' + msg
        self.__log(
            datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")+" \n\t[LOG] @" + logString)
        print(Fore.BLUE + logString + Style.RESET_ALL)

    def warn(self, msg: str):
        logString: str = '[' + self.scope + '] : ' + msg
        self.__log(
            datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")+" \n\t[WARN] @" + logString)
        print(Fore.YELLOW + logString + Style.RESET_ALL)

    def error(self, msg: str):
        logString: str = '[' + self.scope + '] : ' + msg
        self.__log(
            datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")+" \n\t[ERROR] @" + logString)
        print(Fore.RED + logString + Style.RESET_ALL)

    def __log(self, msg: str):
        file1 = open("myfile.txt", "a")
        file1.write(msg+'\n')
        file1.close()
        pass
