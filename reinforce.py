import numpy as np
import random
import matplotlib.pyplot as plt
#Payoffs
a=3
b=3
c=0
d=0
e=0
f=0
g=0
h=0
k=5
l=5
m=0
n=0
q=0
r=0
s=0
t=0
u=2
v=2

#EWA Parameters
Ainit=[1,1,1]

#Attraction rule parameters
phi=1
kappa=1
delta=0
N=[1]
lamb=0.2

#A is period*A each period
A=[[1,1,1,1,1,1]]
p1=[]
p2=[]
outcome=[]
maxperiod=100
A_col=Ainit
A_row=Ainit
for i in range(maxperiod-1):
    #row player
    p1r=np.exp(lamb*A_row[0])/(np.exp(lamb*A_row[0])+np.exp(lamb*A_row[1])+np.exp(lamb*A_row[2]))
    p2r=np.exp(lamb*A_row[1])/(np.exp(lamb*A_row[0])+np.exp(lamb*A_row[1])+np.exp(lamb*A_row[2]))
    p3r=np.exp(lamb*A_row[2])/(np.exp(lamb*A_row[0])+np.exp(lamb*A_row[1])+np.exp(lamb*A_row[2]))

    rand1=random.random()
    if rand1<p1r:
        row_choice=1
    elif rand1>=p1r + p2r:
        row_choice=3
    else:
        row_choice=2
    
    #column player
    p1c=np.exp(lamb*A_col[0])/(np.exp(lamb*A_col[0])+np.exp(lamb*A_col[1])+np.exp(lamb*A_col[2]))
    p2c=np.exp(lamb*A_col[1])/(np.exp(lamb*A_col[0])+np.exp(lamb*A_col[1])+np.exp(lamb*A_col[2]))
    p3c=np.exp(lamb*A_col[2])/(np.exp(lamb*A_col[0])+np.exp(lamb*A_col[1])+np.exp(lamb*A_col[2]))

    p1.append(p1c)
    p2.append(p2c)

    rand2=random.random()
    if rand2<p1c:
        col_choice=1
    elif rand2>=p1c+p2c:
        col_choice=3
    else:
        col_choice=2
    
    if row_choice==1 and col_choice==1:
        outcome.append(1)
    if row_choice==1 and col_choice==2:
        outcome.append(2)
    if row_choice==1 and col_choice==3:
        outcome.append(3)
    if row_choice==2 and col_choice==1:
        outcome.append(4)
    if row_choice==2 and col_choice==2:
        outcome.append(5)
    if row_choice==2 and col_choice==3:
        outcome.append(6)
    if row_choice==3 and col_choice==1:
        outcome.append(7)
    if row_choice==3 and col_choice==2:
        outcome.append(8)
    if row_choice==3 and col_choice==3:
        outcome.append(9)

    #indicators
    row_indicators=[0,0,0]
    row_indicators[row_choice-1]=1

    col_indicators=[0,0,0]
    col_indicators[col_choice-1]=1

    N.append(phi*(1-kappa)*N[i] +1)

    A_row[0]=(phi*N[i]*A_row[0]+(delta*(col_indicators[0]*a+col_indicators[1]*c+col_indicators[2]*e)+(1-delta)*(row_indicators[0]*col_indicators[0]*a+row_indicators[0]*col_indicators[1]*c+row_indicators[0]*col_indicators[2]*e))/N[i+1])
    A_row[1]=(phi*N[i]*A_row[1]+(delta*(col_indicators[0]*g+col_indicators[1]*k+col_indicators[2]*m)+(1-delta)*(row_indicators[1]*col_indicators[0]*g+row_indicators[1]*col_indicators[1]*k+row_indicators[1]*col_indicators[2]*m))/N[i+1])
    A_row[2]=(phi*N[i]*A_row[2]+(delta*(col_indicators[0]*q+col_indicators[1]*s+col_indicators[2]*u)+(1-delta)*(row_indicators[2]*col_indicators[0]*q+row_indicators[2]*col_indicators[1]*s+row_indicators[2]*col_indicators[2]*u))/N[i+1])

    A_col[0]=(phi*N[i]*A_col[0]+(delta*(row_indicators[0]*b+row_indicators[1]*h+row_indicators[2]*r)+(1-delta)*(col_indicators[0]*row_indicators[0]*b+col_indicators[0]*row_indicators[1]*h+col_indicators[0]*row_indicators[2]*r))/N[i+1])
    A_col[1]=(phi*N[i]*A_col[1]+(delta*(row_indicators[0]*d+row_indicators[1]*l+row_indicators[2]*t)+(1-delta)*(col_indicators[1]*row_indicators[0]*d+col_indicators[1]*row_indicators[1]*l+col_indicators[1]*row_indicators[2]*t))/N[i+1])
    A_col[2]=(phi*N[i]*A_col[2]+(delta*(row_indicators[0]*f+row_indicators[1]*n+row_indicators[2]*v)+(1-delta)*(col_indicators[2]*row_indicators[0]*f+col_indicators[2]*row_indicators[1]*n+col_indicators[2]*row_indicators[2]*v))/N[i+1])
    A.append([A_row[0],A_row[1],A_row[2],A_col[0],A_col[1],A_col[2]])


plt.plot(outcome)
#plt.plot(np.add(p1,p2))
#plt.plot(p1)
plt.ylim(0, 10)
plt.show()
#print(A)
#print(np.add(p1,p2))
