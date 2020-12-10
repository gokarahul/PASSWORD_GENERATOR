import random

def dicenumber():
    diceout = ""
    for i in range(5): # 5 dice rolls
        diceout += str(random.randrange(5) + 1) # add result of dice roll to variable
    return diceout

def diceware(x):
    wordlist = open('dictionary.txt', 'r')
    for line in wordlist:
        if line.startswith(x):
            wordlist.close()
            return line.lstrip('123456\t')

limit = int(input("How many words do you want in your password : "))

pswd = ''

for i in range(limit): 
    pswd += diceware(dicenumber()).strip('\n') + ' ' # increase number for longer passphrases

print(pswd)