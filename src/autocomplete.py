# -*- coding: utf -8 -*-

from __future__ import unicode_literals
from trie import Trie


class Autocomplete(object):
    """Callable autocomplete class takes a list to create word_list."""

    def __init__(self, words, max_completions=5):
        """Initialize the class with a dictionary."""
        self.max_completions = int(max_completions)
        self.trie = Trie()
        self.words = words
        for word in self.words:
            self.trie.insert(word)

    def __call__(self, word):
        """Return a list of matches that will complete word."""
        return self.trie.traverse(word, self.max_completions)
