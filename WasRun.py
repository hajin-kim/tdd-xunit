from TestCase import TestCase


class WasRun(TestCase):
    def __init__(self, name):
        self.wasRun = False
        self.name = name

    def testMethod(self):
        self.wasRun = True

    def run(self):
        method = getattr(self, self.name)
        method()
