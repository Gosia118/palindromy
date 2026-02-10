

def my_word(word):
    my_word_1 = word[0:]
    my_word_2 = word[::-1]
    return my_word_1 == my_word_2
    
my_word("potop")
print(my_word("potop"))
