# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
import logging
import sys
import unittest


# Pytest specific test, but pytest will pick up on both tests
def test_logging2(caplog):
    logger = logging.getLogger(__name__)
    # caplog.set_level(logging.DEBUG)  # Debug level
    caplog.set_level(logging.ERROR)  # Error level

    logger.debug("This is a debug message.")
    logger.info("This is an info message.")
    logger.warning("This is a warning message.")
    logger.error("This is an error message.")
    logger.critical("This is a critical message.")

    # Printing to stdout and stderr
    print("This is a stdout message.")
    print("This is a stderr message.", file=sys.stderr)
    assert False


# Unittest specific test, unittest will only see this test while pytest will see both tests
class TestLogger(unittest.TestCase):
    def test_logging(self):
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)  # Set the desired log level
        # logger.setLevel(logging.ERROR)  # Set the desired log level

        logger.debug("This is a debug message in a unittest.")
        logger.info("This is an info message in a unittest.")
        logger.warning("This is a warning message in a unittest.")
        logger.error("This is an error message in a unittest.")
        logger.critical("This is a critical message in a unittest.")

        # Printing to stdout and stderr
        print("This is a stdout message.")
        print("This is a stderr message.", file=sys.stderr)
