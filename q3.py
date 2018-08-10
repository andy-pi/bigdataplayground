import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from linearreg import linearscatter


data = pd.read_csv("DataFinalAssignment2016.csv")

Xpupq4=[]
Xpupq15=[]

for i in range (len(data.age)):
    Xpupq4.append(data.pupq4[i])
    Xpupq15.append(data.pupq15[i])

#Xpupq4=[10,12,12,4,6,2,1,0]
#Xpupq15=[67,23,33,33,23,20,15,10]

fig, ax = plt.subplots()
plt.xlabel("pupq4")
plt.ylabel("pupq15")


x = np.array(Xpupq15)#np.random.randn(n)
y = np.array(Xpupq4)#x * np.random.randn(n)

fig, ax = plt.subplots()
fit = np.polyfit(x, y, deg=1)
ax.plot(x, fit[0] * x + fit[1], color='red')
ax.scatter(x, y)


#ax.scatter(,Xpupq4)

fig.savefig('satis.svg')

(ax, model, fig) = linearscatter(x, y, ax=None)
ax.set_xlabel("pupq4")
ax.set_ylabel("pupq15")
r2 = model.score(np.reshape(x, (len(x), 1)), y)
ax.set_title('Linear regression (R2 = %.2f)' % r2)
fig.savefig('regr.svg')