import os
import glob
import json
import unittest

from JSONMemoizer import JSONMemoize 

TEST_FILES_GLOB="/tmp/TestJSONMemoizer*.json"
TEST_JSON_FILENAME="/tmp/TestJSONMemoizer.json"
TEST_ARGS_JSON_FILENAME="/tmp/TestJSONMemoizer-%.json"

@JSONMemoize(TEST_JSON_FILENAME)
def memoizedFunction():
    return 42

@JSONMemoize(TEST_ARGS_JSON_FILENAME)
def memoizedFunctionWithArg(x):
    return 42 + x

class TestJSONMemoizer(unittest.TestCase):

    def tearDown(self):
        for f in glob.glob(TEST_FILES_GLOB):
            os.remove(f)

    def test_invocationReturnsResultOfFunction(self):
        self.assertEqual(42, memoizedFunction())

    def test_resultOfInvocationIsSavedToFile(self):
        memoizedFunction()
        with open(TEST_JSON_FILENAME) as f:
            self.assertEqual(42, json.loads(f.read()))

    def test_valueFromFileIsReturnedRegardlessOfFunction(self):
        with open(TEST_JSON_FILENAME, "w") as f:
            f.write(json.dumps(15))
        self.assertEqual(15, memoizedFunction())

    def test_memoizeFunctionWithArgument(self):
        self.assertEqual(44, memoizedFunctionWithArg(2))

    def test_memoizeFunctionWithDifferentArgument(self):
        self.assertEqual(44, memoizedFunctionWithArg(2))
        self.assertEqual(45, memoizedFunctionWithArg(3))
