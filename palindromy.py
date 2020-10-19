# Moduł 4
# Zadanie 1
'''
list.reverse()
list.index(x[, start[, end]])

'''

def palindrom(word):
    #reversed_word = reversed(word)
    #reversed_word = word.reverse()
    #print(str(reversed_word))
    count = 1
    for leter in word:
        first_to_equal = word[count - 1]
        second_to_equal = word[-count]
        print(f"pierwsza to {first_to_equal}, druga to {second_to_equal}")
        count = count + 1
    return

print()
