from colorama import Fore, Style


class Logger:
    def __init__(self, scope: str) -> None:
        self.scope = scope or ""
        pass

    def log(self, msg: str) -> None:
        logString: str = '[' + self.scope + '] : ' + msg
        print(Fore.BLUE + logString + Style.RESET_ALL)

    def warn(self, msg: str) -> None:
        logString: str = '[' + self.scope + '] : ' + msg
        print(Fore.YELLOW + logString + Style.RESET_ALL)

    def error(self, msg: str) -> None:
        logString: str = '[' + self.scope + '] : ' + msg
        print(Fore.RED + logString + Style.RESET_ALL)
