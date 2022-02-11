import matplotlib.pyplot
import numpy as np
import functions1
import matplotlib.pyplot as plt
from functions1 import success

#The x values are the period of the game, or known as the amount of times the coin can be flipped
x=[0,10,20,30,40,50,60,70,80,90,100]
#the a values are the averages of the games played for each period.

#Main Array Being used
a = []

#Subarrays being used, each subarray is one game
a1 = []



#The game for a1
for period in x:
    #Gets all the values of the game
    tota=functions1.ngames(1000,period)
    #the array gets appended with the values of each period repeated 10,000 times, and gets the average
    a1.append(tota/1000)

#Converting arrays into numpy arrays for caluclations
arr1 = np.array(a1)



z = [(success) * 0,(success) * 10,(success) * 20,(success) * 30,(success) *40,(success) *50, (success) * 60,(success) * 70,(success) * 80,(success) * 90,(success) * 100]

values = range(len(x))
plt.title('St. Petersburg Gamble')
plt.ylabel('Average Return')
plt.xlabel('Length of Game')
plt.plot(x,a1,marker="o", label=' Game')
plt.ylim([0,100])
plt.plot(x,z, marker="o",label=' Expcted Output')
plt.show()