#!/usr/bin/python
import unittest
import os
from publisher import publisher
from hashlib import md5
import sys

# test methods from publisher.py

# execute single test
# nosetests publisher_test.py -- single test
# nosetests /path/to/folder -- suit of test

class publisher_test(unittest.TestCase):

    def test_hello(self):
        pp = publisher('dropbox')
        result = pp.hello()
        self.assertEqual(result, 0)

    def test_publish(self):
        pp = publisher('dropbox')
        result = pp.publish('sample/sample.txt', '/')
        self.assertEqual(result, 0)  # 0 means published successfully

    @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
    def test_publish_exists(self):
        pp = publisher('dropbox')
        os.remove('sample_response/sample.txt')

        result = pp.download('/sample.txt', 'sample_response/sample.txt')
        self.assertEqual(result, 0)
        response_hash = md5(open('sample_response/sample.txt', 'rb').read()).hexdigest()
        original_hash = md5(open('sample/sample.txt', 'rb').read()).hexdigest()
        self.assertEqual(response_hash, original_hash)
        # python check if md5 of [sample/sample.txt] [sample_response/sample.txt] match


