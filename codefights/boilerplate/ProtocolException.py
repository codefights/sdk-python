class ProtocolException(Exception):

    __module__ = None

    def __init__(self, message):
        self.msg = message
        self.code = 0

    def __str__(self):
        return '[' + str(self.code) + ']: {' + self.msg + '}'

    def __repr__(self):
        return self.__str__()