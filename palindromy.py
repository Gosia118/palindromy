

def my_word(word):
    my_word_1 = word[0:]
    my_word_2 = word[::-1]
    if my_word_1 == my_word_2:
        print("Podany wyraz: %s jest palindromem" % word)
    else:
        print("Podany wyraz: %s nie jest palindromem" % word)
    

my_word("potop")

