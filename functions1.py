import random
success = float(input("Type in the Percent Parameter of Success: "))

def test():
    if random.random() < success:
        return True
    else:
        return False

def game(period):
    retur=1
    count=0
    while test()==True and count<period:
        retur*=2
        count+=1
    return retur

def ngames(n,period):
    tot=0
    for i in range(n):
        tot+=game(period)
    return tot