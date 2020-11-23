from collections import Counter
import re
from string import punctuation
from typing import List, Optional


def word_count(content: str, *args, **kwargs) -> Optional[str]:

    content = content.strip()

    if not content:
        return

    raw_word_split: List[str] = content.split()

    if not raw_word_split:
        return

    counter = Counter(raw_word_split)

    punctuation_and_digits_only_pattern = fr"^[{punctuation}\d]+$"
    word_keys = counter.keys()
    to_remove = []
    for key in word_keys:
        if re.match(punctuation_and_digits_only_pattern, key):
            to_remove.append(key)

    for not_valid in to_remove:
        del counter[not_valid]

    words = len(list(counter.elements()))

    if not words:
        return "Found no valid word in text, see rules."

    a_word = "Found a word in text."

    return f"Found {words} words in text." if words > 1 else a_word
