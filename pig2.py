def pig(word):
    x = list("aieou")
    y = len(word)
    z = word.lower()
    for i in range(y):
        if z[0] in x:
            print(word + "yay")
            break
        elif z[i] in x:
            print(word[i:]+word[:i]+"ay")
            break
        else:
            pass
 
while True:
    word = str(input("input word \n"))
    if (word.isalpha()):
        pig(word)
        break
    else:
        print("input a word pls")

