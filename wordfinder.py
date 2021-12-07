"""Word Finder: finds random words from a dictionary."""

import random


class WordFinder:
    """Random word finder from dictionary.

    >>> wf = WordFinder("randomwords.txt")
    3 words read

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True
    """

    def __init__(self, path):
        """Reads the dictionary and returns the number of words read."""

        dict = open(path)
        self.words = self.parse(dict)
        print(f"{len(self.words)} words read")

    def parse(self, dict_file):
        """Parse dict into list of words."""
        return [w.strip() for w in dict_file]

    def random(self):
        """Return random word."""
        return random.choice(self.words)


class SpecialWordFinder(WordFinder):
    """Specialized WordFinder that excludes blank lines/comments.

    >>> swf = SpecialWordFinder("specialwords.txt")
    4 words read

    >>> swf.random() in ["kale", "parsnips", "apple", "mango"]
    True

    >>> swf.random() in ["kale", "parsnips", "apple", "mango"]
    True

    >>> swf.random() in ["kale", "parsnips", "apple", "mango"]
    True
    """

    def parse(self, dict):
        """Parse dict into list of words skipping comments and blanks."""
        return [w.strip() for w in dict
                if w.strip() and not w.startswith("#")]
