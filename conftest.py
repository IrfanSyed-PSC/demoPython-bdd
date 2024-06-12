import logging
import pytest
import urllib3
import os



@pytest.fixture(autouse=True)
def set_log_level():
    logging.getLogger('urllib3').setLevel(logging.ERROR)
    logging.getLogger().setLevel(logging.DEBUG)

@pytest.fixture(autouse=True)
def disable_warnings():
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
