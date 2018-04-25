import json
import time
import unittest
from planet.tasks import *

class TestTasks(unittest.TestCase):
    config = json.load(open('config.json'))

    def test_writeToS3(self):
        data = "Test data written by a dev"
        bucketname = self.config["Resources"]["dev"]["s3-bucket"]
        t = time.localtime()
        filename = 'test-%d-%d-%d %d:%d.dat' % (t.tm_year,t.tm_mon,t.tm_mday,t.tm_hour,t.tm_min)
        key = self.config["Resources"]["dev"]["s3-folder"] + filename
        writeToS3(data, bucketname, key)
        print("test1")
        self.assertTrue(filename)

