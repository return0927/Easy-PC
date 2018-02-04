from json import load


class SetManager:
    def __dict__(self):
        return self.set

    def __init__(self, defaults=None):
        self.set = {}

        if defaults and isinstance(defaults, type(dict())):
            for key in defaults.keys():
                self.set[key] = defaults[key]
        else:
            self.set = load(open("./sub/settings.json", "r", encoding="UTF-8"))

    def get(self, key=""):
        if key:
            return SetManager(self.set[key])
        else:
            return self.__dict__()
