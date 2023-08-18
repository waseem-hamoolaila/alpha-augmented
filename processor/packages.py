"""
In this file we will proved hard coded packages..
Only for the ease of demoing.
"""

from .fitting_utils import Package

packages = [
    Package([[1, 1, 1, 1]]),
    Package([[1, 1, 1, 0], [0, 1, 1, 1]]),
    Package([[0, 1, 1, 0], [0, 1, 0, 1]]),
    Package([[1, 1], [1, 1]]),
    Package([[1], [1], [1], [1]]),
]
