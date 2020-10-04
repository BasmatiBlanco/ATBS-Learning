spam = ['apples', 'bananas', 'tofu', 'cats']

def separa(lis):
    new = ""
    for i in range(len(spam)):
        new += spam[i] + ", " 
    new += spam[-1] + "."
    print (new)

