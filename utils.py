"""
This module will hold the utility functions needed for blockchain
"""

from datetime import datetime


def get_current_timestamp():
    return datetime.now().strftime("%Y%m%d%H%M%S%f")