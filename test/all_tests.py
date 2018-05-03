import unittest
from test.test_api import TestApi
from test.test_tasks import TestTasks

api = TestApi()
tasks = TestTasks()
alltests = unittest.TestSuite((api.suite(), tasks.suite()))

if __name__ == '__main__':
    unittest.main()
