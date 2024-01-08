from TestCase import TestCase


class WasRun(TestCase):
    def __init__(self, name):
        TestCase.__init__(self, name)

    def setUp(self):
        self.wasRun = False
        self.wasSetUp = True
        self.log = "setUp "

    def testMethod(self):
        self.wasRun = True
