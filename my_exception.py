class FormatError(Exception):
    def __init__(self, arg):
        self.value = arg

    def __str__(self):
        return repr(self.value)
