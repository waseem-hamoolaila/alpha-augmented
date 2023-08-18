"""
In this file we will proved hard coded packages..
Only for the ease of demoing.
"""

from .fitting_utils import Package

packages = [
    Package([[1, 1, 1, 1]], color="#0ee607", identifier=1),
    Package([[1, 1, 1, 0], [0, 1, 1, 1]], color="#d11717", identifier=2),
    Package([[0, 1, 1, 0], [0, 1, 0, 1]], color="#284cb8", identifier=3),
    Package([[1, 1], [1, 1]], color="#9928b8", identifier=4),
    Package([[1], [1], [1], [1]], color="#289eb8", identifier=5),
]
