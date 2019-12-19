

class MazeException(Exception):
    def __init__(self):
        self.mazeMess = ""

    def message(self, strMess):
        self.mazeMess = self.mazeMess+strMess

    def getMessage(self):
        return self.mazeMess