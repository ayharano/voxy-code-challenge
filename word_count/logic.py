import re
from typing import List, Optional


def word_count(content: str, *args, **kwargs) -> Optional[str]:

    content = content.strip()

    if not content:
        return

    raw_word_split: List[str] = content.split()

    if not raw_word_split:
        return

    words = len(raw_word_split)

    a_word = "Found a word in text."

    return f"Found {words} words in text." if words > 1 else a_word
