# Moduł 4
# Zadanie 1


def palindrom(word):
    count = 1
    list_reversed_word = []
    list_word = []
    for leter in word:
        leter_from_begining = word[count - 1]
        leter_from_end= word[-count]
        list_word.append(leter_from_begining)
        list_reversed_word.append(leter_from_end)
        count = count + 1
    if list_word == list_reversed_word:
        result = True
    else:
        result = False
    return result



print()
