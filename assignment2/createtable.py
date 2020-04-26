
import requests
from db import *

def test_createtestTable():
    createTestsTable()

def test_createSubmissiontable():
    createScantronAnswersTable()

if __name__ == "__main__":
    test_createtestTable()
    test_createSubmissiontable()