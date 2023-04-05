from .Logger import Logger
from collections.abc import Callable


class VIDEO_PROCESSOR_CONSTANTS_CLASS:
    def __init__(self) -> None:
        self.Logger = Logger("VIDEO_PROCESSOR_CONSTANTS")
        self.values = {
            # "VIDEO_PATH": {
            #     "listeners": [{
            #         "id": "",
            #         "cb": None
            #     }],
            #     "value": "C:/Users/91911/Documents/JDownloader/Miley Cyrus - Flowers (Official Video) (1406p_24fps_AV1-128kbit_AAC).mp4"
            # }
        }
        pass

    def create(self, property, value) -> None:
        self.values[property] = {"value": value, "listeners": [{
            "id": "",
            "cb": None
        }]}
        pass

    def use(self, property: str):
        return self.values[property]["value"]

    def addListener(self, property: str, id: str, function: Callable):
        ids = map(lambda x: x["id"], self.values[property]["listeners"])
        if id not in list(ids):
            self.values[property]["listeners"].append({
                "id": id,
                "cb": function
            })
        else:
            self.Logger.error('Failed to add listener for '+property +
                              ' Listener with id "'+id+'" already exists.')

    def update(self, property: str, value):
        if property in list(self.values.keys()):
            self.values[property]["value"] = value
            for l in self.values[property]["listeners"]:
                if l["cb"] is not None:
                    l["cb"](value)
        else:
            self.Logger.error('Failed to update.Make sure you have created "' +
                              property + '" by using create method.')
