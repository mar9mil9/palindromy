# Moduł 4
# Zadanie 1
'''
list.reverse()
list.index(x[, start[, end]])

'''

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
        print(f"{word} to palindrom")
    else:
        print(f"{word} nie jest palindromem")
    return

print()
