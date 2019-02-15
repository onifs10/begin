def pig(word):
    x = list(word)
    z = list("aeiou")
    y = list("bcdfghjklmnpqrstvwxyz")
    if (x[0] in z):
        print("use any of this")
        print(word + "way" )
        print(word + "yay")
        print(word + "ay")
        print(word[2:] + word[0:2]+"ay")
    if (x[0] in y and x[1] in y and x[3] in y):
        print(word[3:]+word[0:3]+"ay")
    elif(x[0] in y and x[1] in y):
        print(word[2:]+word[0:2]+"ay")
    elif(x[0] in y ):
        print(word[1:]+word[0]+"ay")
while True:
    word = str(input("input word \n"))
    if (word.isalpha()):
        pig(word)
        break
    else:
        print("input a word pls")

print("live")