from colorama import Fore, Style


class Logger:
    def __init__(self, scope: str) -> None:
        self.scope = scope or ""
        pass

    def log(self, msg: str) -> None:
        logString: str = '[' + self.scope + '] : ' + msg
        self.__log("[LOG]" + msg)
        print(Fore.BLUE + logString + Style.RESET_ALL)

    def warn(self, msg: str) -> None:
        logString: str = '[' + self.scope + '] : ' + msg
        self.__log("[WARN]" + msg)
        print(Fore.YELLOW + logString + Style.RESET_ALL)

    def error(self, msg: str) -> None:
        logString: str = '[' + self.scope + '] : ' + msg
        self.__log("[ERROR]" + msg)
        print(Fore.RED + logString + Style.RESET_ALL)

    def __log(self, msg: str):
        # Stuff like writing to a file or posting to server goes here.
        pass
