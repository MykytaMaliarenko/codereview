"""
Вивести усі слова де є '9'
"""
text = "a9da adas da dasdd3 we9ssedfes fsrf435345 3 erter"
words = text.split()
i = 0
while i < len(words):
    word = words[i]
    if word.__contains__("9"):
        print(word)

    i += 1
