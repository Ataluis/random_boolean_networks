import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import math
from collections import defaultdict
from itertools import islice

#plot settings
plt.rcParams.update({
    "text.usetex": True,
    "font.size" : 16
})

#Grid
fig = plt.figure(figsize=(12,6))
histo_color = 'silver'
basin_color = 'orangered'
garden_color = 'yellowgreen'

gridbool = False
setticks = False

gs = gridspec.GridSpec(1, 2)
#-----------------------------------------------------------------------
ax1 = plt.subplot(gs[0,0])
ax2 = plt.subplot(gs[0,1])

if gridbool:
    ax1.grid(True)
    ax2.grid(True)

if setticks:
    ax1.set_xticks([0,10,20,30,40,50])
    ax2.set_xticks([0,10,20,30,40,50])

N = 20000000
data = []
with open("basin_of_attraction_master_N10_K_10.dat") as fobj:
    counter = 0
    for line in fobj:
        data.append([float(i) for i in line.split(' ') if not i == '\n'])
        counter += 1
        if counter == N: break
    #data = [[float(num) for num in line.split()] for line in fobj]

basin = defaultdict(list)
garden_eden = defaultdict(list)

num_elements = 0
for vec in data:
    basin[vec[3]].append(vec[10]/(np.power(2,vec[0])))
    garden_eden[vec[3]].append(vec[11]/(np.power(2,vec[0])))
    num_elements += 1

L =[]
NB =[]
NG =[]
prob = []
Y = []

for key in basin:
    L.append(key)
    length = float(len(basin[key]))
    NB.append(sum(basin[key])/length)
    NG.append(sum(garden_eden[key])/length)
    prob.append(length/num_elements)
    
C = prob[0]
for i, l in enumerate(L):
  Y.append((-2*2**10)*np.log(l*prob[i]/C))



ax1.bar(L,Y,color=histo_color)#,alpha=0.8)
X = np.arange(1,max(L[:100]),0.1)

ax1.plot(X,X**2,'r', ls='-.', lw=2)
ax1.set_xlim(0,100)
ax1.set_ylim(0,12000)
ax1.set(xlabel=r'$L$', ylabel=r'$-2\Omega\cdot\ln{\left(L\cdot\left\langle N_c (L)\right\rangle\right)}$')

ax2.bar(L,prob,color=histo_color)#,alpha=0.8)
X = np.arange(1,max(L[:100]),0.1)

ax2.plot(X,C*np.exp(-X**2/(2*2**10))/X,'r', ls='-.', lw=2)
ax2.set_xlim(0,100)
ax2.set_ylim(1e-8,1)
ax2.set(xlabel=r'$L$', ylabel=r'$P(L)$', yscale='log')
#-----------------------------------------------------------------------

plt.tight_layout()
plt.show()
# ~ fig.savefig("Basin_N"+text+".pdf")
