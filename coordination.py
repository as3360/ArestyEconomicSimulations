import random
import matplotlib.pyplot as plt
N=100
a=1.01
b=1
c=0
d=0
epsilon=0.05
maxperiod=100
initial_proportion=0.1

qstar=(b-c)/(a-d+b-c)
print(qstar)
choise_history=[]
for i in range(N):
    rand=random.random()
    if rand<initial_proportion:
        choise_history.append(1)
    else:
        choise_history.append(0)

k0=sum(choise_history)
kt=[k0]
for i in range(maxperiod):

    q=[]
    for j in range(N-1):
        q.append((choise_history[j-1]+choise_history[j+1])/2)
    q.append((choise_history[0]+choise_history[N-2])/2)

    I=[]
    for j in range(N):
        if q[j]>=qstar:
            I.append(1)
        else:
            I.append(0)


    new_choice_history=[]
    for j in range(N):
        rand1=random.random()
        rand2=random.random()
     
        if rand1<1-2*epsilon:
            new_choice_history.append(I[j])
        elif rand2<0.5:
            new_choice_history.append(1)
        else:
            new_choice_history.append(0)

    kt.append(sum(new_choice_history))
    choise_history=new_choice_history
ktprint=[i/N for i in kt]
plt.plot(ktprint)
plt.ylim(0, 1)
plt.show()
