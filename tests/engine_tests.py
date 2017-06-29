from nose.tools import *
import spork.engine


def setup():
    print("SETUP")


def teardown():
    print("TEAR DOWN")


def test_basic():
    print("I RAN!", end='')
