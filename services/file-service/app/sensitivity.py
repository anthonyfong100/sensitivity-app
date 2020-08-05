import re

sensitivty_mapping = {
    "secret": 10,
    "dathena": 7,
    "internal": 5,
    "external": 3,
    "public": 1,
}


def count_occurance(sentence: str, word: str) -> int:
    return len(re.findall(word, sentence, re.IGNORECASE))


def calculate_sensitivity_score(sentece: str) -> int:
    value = 0
    for word in sensitivty_mapping.keys():
        count = count_occurance(sentece, word)
        value += sensitivty_mapping[word] * count
    return value
