class Event(object):

    def __init__(self):
        self._event_handlers = []

    def Register(self, event_handler):
        self._event_handlers += [event_handler]

    def Raise(self, *args):
        for event_handler in self._event_handlers:
            event_handler(*args)
