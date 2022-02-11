import antfunction
import matplotlib.pyplot as plt

startk=50000
maxn=100000
k=[startk]
epsilon=0.15
delta=0.3
n=[1]



for i in range(maxn):
    k.append(antfunction.antgame(k[i],maxn,epsilon,delta)+k[i])
    n.append(n[i]+1)

plt.plot(n,k)
plt.show()