import random

def antgame(k,n,epsilon,delta):
    probab_plus=(1-k/n)*(epsilon+(1-delta)*k/(n-1))
    probab_minus=(k/n)*(epsilon+(1-delta)*(n-k)/(n-1))
    test=random.random()

    if test<probab_plus:
        return 1
    elif test>(1-probab_minus):
        return -1
    else:
        return 0