################ matplotlib
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
pop=[1984, 1985, 1986, 1988]
year=[40, 50, 70,120]

fig, ax = plt.subplots()
ax.plot(pop, year)
fig.savefig('display.svg')


import pandas as pd
data = pd.read_csv("DataFinalAssignment2016.csv")

#ages=[]
numtdecavs=[]
for i in range (len(data.age)):
    #ages.append(data.age[i])
    numtdecavs.append(data.numtdecav[i])


fig, ax = plt.subplots()
ax.plot(numtdecavs)
fig.savefig('display.svg')

# frequency of numbdecatv
fig2, ax2 = plt.subplots()
freq=data.numtdecav.value_counts()
ax2.plot(freq)
fig2.savefig('display2.svg')


list_1=['12','15']
#print(data.age)
data = data[data.age.isin(list_1)]
#
#print(data.age)

#fig3, ax3 = plt.subplots()
#ax3.boxplot(data.numtdecav)
#fig3.savefig('display3.svg')
