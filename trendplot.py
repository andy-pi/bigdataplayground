import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd


def trendline(xd, yd, order=1, c='r', alpha=1):
    """Make a line of best fit"""

    #Calculate trendline
    coeffs = np.polyfit(xd, yd, order)

    intercept = coeffs[-1]
    slope = coeffs[-2]
    power = coeffs[0] if order == 2 else 0

    minxd = np.min(xd)
    maxxd = np.max(xd)

    xl = np.array([minxd, maxxd])
    yl = power * xl ** 2 + slope * xl + intercept

    # add the trendline to the axis
    fig, ax = plt.subplots()
    ax.plot(xl, yl, c, alpha=alpha)
    ax.scatter(xd, yd)
    
    # Calculate R Squared
    p = np.poly1d(coeffs)
    ybar = np.sum(yd) / len(yd)
    ssreg = np.sum((p(xd) - ybar) ** 2)
    sstot = np.sum((yd - ybar) ** 2)
    Rsqr = ssreg / sstot
    
    return Rsqr, ax, fig
        


data = pd.read_csv("DataFinalAssignment2016.csv")

# for positve values of pupq15 pupq4 only
# 15 yearolds in england only
data = data.drop(data[data.age < 15].index)
data = data.drop(data[data.pupq4 < 0].index)
data = data.drop(data[data.pupq15 < 0].index)

print(data.head(5))

Xpupq4=[]
Xpupq15=[]

for i in range (len(data.age)):
    Xpupq4.append(data.pupq4.iloc[i])
    Xpupq15.append(data.pupq15.iloc[i])

#x=[10,12,12,4,6,2,1,0]
#y=[67,23,33,33,23,20,15,10]

x = np.array(Xpupq15)#np.random.randn(n)
y = np.array(Xpupq4)#x * np.random.randn(n)

Rsqr, ax, fig = trendline(x, y, order=1, c='r', alpha=1)


ax.set_xlabel("Satisfaction with appearance - pupq4")
ax.set_ylabel("Frequency of brushing - pupq15")
ax.set_title('Trendplot - R^2 = %s' %Rsqr)
fig.savefig('trendplot.svg')

