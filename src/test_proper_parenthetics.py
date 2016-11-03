"""Test file for proper_parenthetics function in proper_parenthetics.py ."""

import pytest
import proper_parenthetics as p

INPUTS = [
    ('())', -1),
    ('))((', -1),
    ('(()()))', -1),
    ('', 0),
    ('()', 0),
    ('()((()))()', 0),
    ('(())()', 0),
    ('((()))', 0),
    ('(()())(', 1),
    ('((()))(', 1)
]


@pytest.mark.parametrize('inputs, result', INPUTS)
def test_proper_parenthetics(inputs, result):
    assert p.proper_parenthetics(inputs) == result
