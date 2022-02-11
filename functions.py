import random

success = float(input("Type in the Percent Parameter of Success: "))

def test():
    if random.random() < (success):
        return True
    else:
        return False

#Flipping of the coin
def game(period):
    retur=0
    count=0
    while count<period:
        if test() == True:
            retur +=1
        elif test() == False:
            retur +=0
        count+=1
    return retur

def ngames(n,period):
    tot=0
    for i in range(n):
        tot+=game(period)
    return tot