"""Test module for Autocomplete class."""

TEST_LIST = [
    'slags',
    'slain',
    'slake',
    'slalom',
    'slam',
    'slims',
    'slimy',
]


def setup_autocompleter(num_results=5):
    from autocomplete import Autocomplete
    a = Autocomplete(TEST_LIST, num_results)
    return a


def test_num_results():
    a = setup_autocompleter()
    results = a('sla')
    assert len(results) == 5


def test_result_words():
    a = setup_autocompleter()
    results = a('sli')
    assert 'slims' in results
