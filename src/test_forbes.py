"""
    Test file for the forbes.py module.
"""

from collections import namedtuple
import pytest
import random
import string

TEST_CASES = [
    {
        "name": "Test Case 1",
        "age": -1,
        "rank": 1,
        "net_worth (USD)": 75000000000,
        "source": "Industry 1",
        "country": "United States"
    },
    {
        "name": "Test Case 2",
        "age": 0,
        "rank": 2,
        "net_worth (USD)": 67000000000,
        "source": "Industry 2",
        "country": "Spain"
    },
    {
        "name": "Test Case 3",
        "age": 25,
        "rank": 3,
        "net_worth (USD)": 60800000000,
        "source": "Industry 3",
        "country": "United States"
    },
    {
        "name": "Test Case 4",
        "age": 25,
        "rank": 1,
        "net_worth (USD)": 60800000000,
        "source": "Industry 4",
        "country": "Mexico"
    },
    {
        "name": "Test Case 5",
        "age": 85,
        "rank": 5,
        "net_worth (USD)": 45200000000,
        "source": "Industry 5",
        "country": "United States"
    },
    {
        "name": "Test Case 6",
        "age": 79,
        "rank": 6,
        "net_worth (USD)": 44200000000,
        "source": "Industry 6",
        "country": "United States"
    },
    {
        "name": "Test Case 7",
        "age": 100,
        "rank": 7,
        "net_worth (USD)": 99200000000,
        "source": "Industry 7",
        "country": "United States"
    }
]


INT_CASES = [random.sample(range(1000),
             random.randrange(2, 100)) for n in range(10)
             ]


STR_CASES = [random.sample(string.printable,
             random.randrange(2, 100)) for n in range(10)
             ]


MySGFix = namedtuple(
    'SGFixture',
    ('graph', 'input_val', 'weight', 'length', 'type_err')
)
