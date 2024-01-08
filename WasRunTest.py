from WasRun import WasRun

test = WasRun("testMethod")
print(test.wasRun)  # False
test.testMethod()
print(test.wasRun)  # True
