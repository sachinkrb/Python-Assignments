def word_game(words):
    t = words
    t1 = t.append("connect")
    t2 = t.append("himself")   
    print(words)
    print(t)
    print(t1)
    print(t2)
    print(t1 is t2)
    print(t is words)

the_word =["John", "can"]
word_game(the_word)
