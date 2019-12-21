"""
Вивести всі слова із найменшим кількістю повторень.
"""
import re


def find_test(text: str) -> list:
    words = re.split(r'[\s\-,|.:!?]', text)
    res = []
    i = 0
    smallest_number_of_repeats = 0
    while i < len(words):
        word = words[i]
        if word == "":
            words.pop(i)
        else:
            count = words.count(word)
            if smallest_number_of_repeats == 0 or count < smallest_number_of_repeats:
                smallest_number_of_repeats = count
                res = [word]
            elif count == smallest_number_of_repeats:
                res.append(word)
            i += 1

    return res


print(find_test("Hello,Hello my dear!"))
