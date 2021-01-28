import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import math
from collections import defaultdict
from itertools import islice

# the data files that we want to compare in our plot
filename1 = "basin_of_attraction_master_N12_K_1_5.dat"
filename2 = "basin_of_attraction_master_N12_K_2.dat"
filename3 = "basin_of_attraction_master_N12_K_12.dat"

# plot settings
plt.rcParams.update({
    "text.usetex": True,
    "font.size" : 16
})

fig = plt.figure(figsize=(12,7))
histo_color = 'navy'
basin_color = 'orangered'
garden_color = 'yellowgreen'

gridbool = True
setticks = False # Decide if you want the [0,10,20,30,40,50] as xticks or the default

gs = gridspec.GridSpec(2, 3, height_ratios=[1.5,1])
#-----------------------------------------------------------------------
ax1 = plt.subplot(gs[0,0])
ax2 = plt.subplot(gs[1,0])

if gridbool:
    ax1.grid(True)
    ax2.grid(True)

if setticks:
    ax1.set_xticks([0,10,20,30,40,50])
    ax2.set_xticks([0,10,20,30,40,50])

N = 10000000
data = []

with open(filename1) as fobj:
    counter = 0
    for line in fobj:
        data.append([float(i) for i in line.split(' ') if not i == '\n'])
        counter += 1
        if counter == N: break
    #data = [[float(num) for num in line.split()] for line in fobj]

# defaultdicts for storing the information about the basin of attraction and garden eden states
basin = defaultdict(list)
garden_eden = defaultdict(list)

# in this step we basically create subsets for each attractor length,
# that we find in the data
num_elements = 0
for vec in data:
    basin[vec[3]].append(vec[10]/(np.power(2,vec[0])))
    garden_eden[vec[3]].append(vec[11]/(np.power(2,vec[0])))
    num_elements += 1

L =[]
NB =[]
NG =[]
prob = []

# here we are averaging the subsets over each attractor length
for key in basin:
    L.append(key)
    length = float(len(basin[key]))
    NB.append(sum(basin[key])/length)
    NG.append(sum(garden_eden[key])/length)
    prob.append(length/num_elements)

# finally we define further informations for the first plots
ax1.set_title(r'$N=12, K=1.5$')
ax1.scatter(L,NB,color=basin_color,label=r'$\mathcal{N}_B$')#alpha=0.5)
ax1.scatter(L,NG,color=garden_color,marker='^',label=r'$\mathcal{N}_G$')#,alpha=0.5)
ax1.set_xlim(0,40)
ax1.set_ylim(0,1)
ax1.set(ylabel=r'$\mathcal{N}_X/\Omega$')
ax1.legend(loc=4)
ax2.bar(L,prob,color=histo_color)#,alpha=0.8)
ax2.set_xlim(0,40)
ax2.set_ylim(1e-8,1)
ax2.set(xlabel=r'$L$', ylabel=r'$P(L)$', yscale='log')
textstring = r'$L_{max}='+str(int(max(L)))+'$'
ax2.text(0.95, 0.94, textstring, horizontalalignment='right', verticalalignment='top', transform=ax2.transAxes)

# from here on we simply repeat the previous steps in order to get the full picture
#-----------------------------------------------------------------------
ax1 = plt.subplot(gs[0,1])
ax2 = plt.subplot(gs[1,1])

if gridbool:
    ax1.grid(True)
    ax2.grid(True)

if setticks:
    ax1.set_xticks([0,10,20,30,40,50])
    ax2.set_xticks([0,10,20,30,40,50])

data = []
with open(filename2) as fobj:
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

for key in basin:
    L.append(key)
    length = float(len(basin[key]))
    NB.append(sum(basin[key])/length)
    NG.append(sum(garden_eden[key])/length)
    prob.append(length/num_elements)



ax1.set_title(r'$N=12, K=2$')
ax1.scatter(L,NB,color=basin_color,label=r'$\mathcal{N}_B$')
ax1.scatter(L,NG,color=garden_color,marker='^',label=r'$\mathcal{N}_G$')#alpha=0.5)
ax1.set_xlim(0,60)
ax1.set_ylim(0,1)
ax1.set(ylabel=r'$\mathcal{N}_X/\Omega$')
ax1.legend(loc=4)
ax2.bar(L,prob,color=histo_color)#,alpha=0.8)
ax2.set_xlim(0,60)
ax2.set_ylim(1e-8,1)
ax2.set(xlabel=r'$L$', ylabel=r'$P(L)$', yscale='log')
textstring = r'$L_{max}='+str(int(max(L)))+'$'
ax2.text(0.95, 0.94, textstring, horizontalalignment='right', verticalalignment='top', transform=ax2.transAxes)
#-----------------------------------------------------------------------
ax1 = plt.subplot(gs[0,2])
ax2 = plt.subplot(gs[1,2])

if gridbool:
    ax1.grid(True)
    ax2.grid(True)

if setticks:
    ax1.set_xticks([0,10,20,30,40,50])
    ax2.set_xticks([0,10,20,30,40,50])

data = []
with open(filename3) as fobj:
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

for key in basin:
    L.append(key)
    length = float(len(basin[key]))
    NB.append(sum(basin[key])/length)
    NG.append(sum(garden_eden[key])/length)
    prob.append(length/num_elements)

ax1.set_title(r'$N=12, K=12$')
ax1.scatter(L,NB,color=basin_color,label=r'$\mathcal{N}_B$')
ax1.scatter(L,NG,color=garden_color,marker='^',label=r'$\mathcal{N}_G$')
ax1.set_xlim(0,100)
ax1.set(ylabel=r'$\mathcal{N}_X/\Omega$')
ax1.legend(loc=2)
ax2.bar(L,prob,color=histo_color)#,alpha=0.8)
ax2.set_xlim(0,100)
ax1.set_ylim(0,1)
ax2.set_ylim(1e-8,1)
ax2.set(xlabel=r'$L$', ylabel=r'$P(L)$', yscale='log')
textstring = r'$L_{max}='+str(int(max(L)))+'$'
ax2.text(0.95, 0.94, textstring, horizontalalignment='right', verticalalignment='top', transform=ax2.transAxes)

# finally plotting everything we have done so far
plt.tight_layout()
plt.show()
# ~ fig.savefig("Basin_N"+text+".pdf")
