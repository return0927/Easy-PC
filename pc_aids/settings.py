from json import dump, load


class SetManager:
    def __dict__(self):
        return self.set

    def __init__(self):
        self.set = {}

        self.get()

    def get(self, part="", key=""):
        self.set = load(open("./sub/settings.json", "r", encoding="UTF-8"))

        if part:
            if key:
                return self.set[part][key]
            else:
                return self.set[part]
        else:
            return self.__dict__()
