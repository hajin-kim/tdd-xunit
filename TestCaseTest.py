from WasRun import WasRun
from TestCase import TestCase


class TestCaseTest(TestCase):
    def testTemplateMethod(self):
        self.test = WasRun("testMethod")
        self.test.run()
        assert ("setUp testMethod " == self.test.log)


TestCaseTest("testTemplateMethod").run()
