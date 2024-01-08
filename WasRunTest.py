from WasRun import WasRun

test = WasRun("testMethod")
print(test.wasRun)  # False
test.run()
print(test.wasRun)  # True
