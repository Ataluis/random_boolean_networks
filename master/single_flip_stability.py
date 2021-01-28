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
fig = plt.figure(figsize=(12,9))
basin_color = 'navy'
garden_color = 'orangered'

gridbool = True
setticks = False

gs = gridspec.GridSpec(3, 3, height_ratios=[1,1,0.7])
#-----------------------------------------------------------------------
ax1 = plt.subplot(gs[0,0])
ax2 = plt.subplot(gs[1,0])
ax3 = plt.subplot(gs[2,0])


if gridbool:
    ax1.grid(True)
    ax2.grid(True)
    ax3.grid(True)

if setticks:
    ax1.set_xticks([0,10,20,30,40,50])
    ax2.set_xticks([0,10,20,30,40,50])
    ax3.set_xticks([0,10,20,30,40,50])

N = 1000000
data = []
with open("basin_of_attraction_master_N12_K_1_5.dat") as fobj:
    counter = 0
    for line in fobj:
        data.append([float(i) for i in line.split(' ') if not i == '\n'])
        counter += 1
        if counter == N: break
    #data = [[float(num) for num in line.split()] for line in fobj]
    
raw_data = defaultdict(list)
other_data = defaultdict(list)

for vec in data:
  if vec[2] > 1:
    if vec[4] > 0:
      raw_data[int(vec[2])].append(float(vec[5])/(vec[3]*vec[4]))
    if vec[7] > 0:
      other_data[int(vec[2])].append(float(vec[8])/(vec[3]*vec[7]))
      
data1 = []
error1 = []
data2 = []
error2 = []
l1 = []
counter = 0
for vec in raw_data.items():
  N = len(vec[1])
  data1.append(sum(vec[1])/N)
  l1.append(vec[0])
  dev = []
  for num in vec[1]:
    dev.append((num-data1[counter])*(num-data1[counter]))
  error1.append(np.sqrt(sum(dev)/N))
  counter+=1


l2 = []
counter = 0
for vec in other_data.items():
  N = len(vec[1])
  data2.append(sum(vec[1])/N)
  l2.append(vec[0])
  dev = []
  for num in vec[1]:
    dev.append((num-data2[counter])*(num-data2[counter]))
  error2.append(np.sqrt(sum(dev)/N))
  counter+=1 

l1, data1 = zip(*sorted(zip(l1, data1)))
l2, data2 = zip(*sorted(zip(l2, data2)))

ax1.set_title(r'$N=12, K=1.5$')
ax1.plot(l1,data1,color=basin_color,label=r'$N_f$')#alpha=0.5)
ax1.plot(l2,data2,color=garden_color,label=r'$N_a$')#alpha=0.5)
ax1.set_xlim(0,30)
ax1.set_ylim(0,1)
ax1.set(ylabel=r'$P(N^{(stable)})$',xlabel='$N_A$')
# ~ ax1.legend(loc=4)

#0NODES, 1DEGREE, 2number_attractors, 3length, 4num_frozen, 5frozen_stable, 6frozen_unstable, 7num_nonfrozen, 8nonfrozen_stable, 9nonfrozen_unstable, 10basin_of_attraction, 11garden_of_eden});

raw_data = defaultdict(list)
other_data = defaultdict(list)
raw_data1 = defaultdict(list)
other_data1 = defaultdict(list)

for vec in data:
  if vec[2] > 1 and vec[3] > 1:
    if vec[4] > 0:
      raw_data[int(vec[3])].append(float(vec[5])/(vec[3]*vec[4]))
    if vec[7] > 0:
      other_data[int(vec[3])].append(float(vec[8])/(vec[3]*vec[7]))
    raw_data1[int(vec[3])].append(float(vec[4])/vec[0])
    other_data1[int(vec[3])].append(float(vec[7])/vec[0])
    
data1 = []
error1 = []
data2 = []
error2 = []
l1 = []
counter = 0
for vec in raw_data.items():
  N = len(vec[1])
  data1.append(sum(vec[1])/N)
  l1.append(vec[0])
  dev = []
  for num in vec[1]:
    dev.append((num-data1[counter])*(num-data1[counter]))
  error1.append(np.sqrt(sum(dev)/N))
  counter+=1


l2 = []
counter = 0
for vec in other_data.items():
  N = len(vec[1])
  data2.append(sum(vec[1])/N)
  l2.append(vec[0])
  dev = []
  for num in vec[1]:
    dev.append((num-data2[counter])*(num-data2[counter]))
  error2.append(np.sqrt(sum(dev)/N))
  counter+=1 

l1, data1 = zip(*sorted(zip(l1, data1)))
l2, data2 = zip(*sorted(zip(l2, data2)))

ax2.plot(l1,data1,color=basin_color,label=r'$N_f$')#alpha=0.5)
ax2.plot(l2,data2,color=garden_color,label=r'$N_a$')#alpha=0.5)
ax2.set_xlim(0,30)
ax2.set_ylim(0,1)
ax2.set(ylabel=r'$P(N^{(stable)})$',xlabel=r'$L$')

data1 = []
error1 = []
data2 = []
error2 = []
l1 = []
counter = 0
for vec in raw_data1.items():
  N = len(vec[1])
  data1.append(sum(vec[1])/N)
  l1.append(vec[0])
  dev = []
  for num in vec[1]:
    dev.append((num-data1[counter])*(num-data1[counter]))
  error1.append(np.sqrt(sum(dev)/N))
  counter+=1


l2 = []
counter = 0
for vec in other_data1.items():
  N = len(vec[1])
  data2.append(sum(vec[1])/N)
  l2.append(vec[0])
  dev = []
  for num in vec[1]:
    dev.append((num-data2[counter])*(num-data2[counter]))
  error2.append(np.sqrt(sum(dev)/N))
  counter+=1 

l1, data1 = zip(*sorted(zip(l1, data1)))
l2, data2 = zip(*sorted(zip(l2, data2)))

ax3.plot(l1,data1,color=basin_color,label=r'$N_f$')#alpha=0.5)
ax3.plot(l2,data2,color=garden_color,label=r'$N_a$')#alpha=0.5)
ax3.set_xlim(0,30)
ax3.set_ylim(0,1)
ax3.set(ylabel=r'$P(N_x)$',xlabel=r'$L$')
# ~ ax2.legend(loc=4)
#-----------------------------------------------------------------------
ax1 = plt.subplot(gs[0,1])
ax2 = plt.subplot(gs[1,1])
ax3 = plt.subplot(gs[2,1])


if gridbool:
    ax1.grid(True)
    ax2.grid(True)
    ax3.grid(True)

if setticks:
    ax1.set_xticks([0,10,20,30,40,50])
    ax2.set_xticks([0,10,20,30,40,50])
    ax3.set_xticks([0,10,20,30,40,50])

N = 1000000
data = []
with open("basin_of_attraction_master_N12_K_2.dat") as fobj:
    counter = 0
    for line in fobj:
        data.append([float(i) for i in line.split(' ') if not i == '\n'])
        counter += 1
        if counter == N: break
    #data = [[float(num) for num in line.split()] for line in fobj]

raw_data = defaultdict(list)
other_data = defaultdict(list)

for vec in data:
  if vec[2] > 1:
    if vec[4] > 0:
      raw_data[int(vec[2])].append(float(vec[5])/(vec[3]*vec[4]))
    if vec[7] > 0:
      other_data[int(vec[2])].append(float(vec[8])/(vec[3]*vec[7]))
      
data1 = []
error1 = []
data2 = []
error2 = []
l1 = []
counter = 0
for vec in raw_data.items():
  N = len(vec[1])
  data1.append(sum(vec[1])/N)
  l1.append(vec[0])
  dev = []
  for num in vec[1]:
    dev.append((num-data1[counter])*(num-data1[counter]))
  error1.append(np.sqrt(sum(dev)/N))
  counter+=1


l2 = []
counter = 0
for vec in other_data.items():
  N = len(vec[1])
  data2.append(sum(vec[1])/N)
  l2.append(vec[0])
  dev = []
  for num in vec[1]:
    dev.append((num-data2[counter])*(num-data2[counter]))
  error2.append(np.sqrt(sum(dev)/N))
  counter+=1 

l1, data1 = zip(*sorted(zip(l1, data1)))
l2, data2 = zip(*sorted(zip(l2, data2)))

ax1.set_title(r'$N=12, K=2$')
ax1.plot(l1,data1,color=basin_color,label=r'$N_f$')#alpha=0.5)
ax1.plot(l2,data2,color=garden_color,label=r'$N_a$')#alpha=0.5)
ax1.set_xlim(0,30)
ax1.set_ylim(0,1)
ax1.set(ylabel=r'$P(N^{(stable)})$',xlabel='$N_A$')
# ~ ax1.legend(loc=4)

#0NODES, 1DEGREE, 2number_attractors, 3length, 4num_frozen, 5frozen_stable, 6frozen_unstable, 7num_nonfrozen, 8nonfrozen_stable, 9nonfrozen_unstable, 10basin_of_attraction, 11garden_of_eden});

raw_data = defaultdict(list)
other_data = defaultdict(list)
raw_data1 = defaultdict(list)
other_data1 = defaultdict(list)

for vec in data:
  if vec[2] > 1 and vec[3] > 1:
    if vec[4] > 0:
      raw_data[int(vec[3])].append(float(vec[5])/(vec[3]*vec[4]))
    if vec[7] > 0:
      other_data[int(vec[3])].append(float(vec[8])/(vec[3]*vec[7]))
    raw_data1[int(vec[3])].append(float(vec[4])/vec[0])
    other_data1[int(vec[3])].append(float(vec[7])/vec[0])
    
data1 = []
error1 = []
data2 = []
error2 = []
l1 = []
counter = 0
for vec in raw_data.items():
  N = len(vec[1])
  data1.append(sum(vec[1])/N)
  l1.append(vec[0])
  dev = []
  for num in vec[1]:
    dev.append((num-data1[counter])*(num-data1[counter]))
  error1.append(np.sqrt(sum(dev)/N))
  counter+=1


l2 = []
counter = 0
for vec in other_data.items():
  N = len(vec[1])
  data2.append(sum(vec[1])/N)
  l2.append(vec[0])
  dev = []
  for num in vec[1]:
    dev.append((num-data2[counter])*(num-data2[counter]))
  error2.append(np.sqrt(sum(dev)/N))
  counter+=1 

l1, data1 = zip(*sorted(zip(l1, data1)))
l2, data2 = zip(*sorted(zip(l2, data2)))

ax2.plot(l1,data1,color=basin_color,label=r'$N_f$')#alpha=0.5)
ax2.plot(l2,data2,color=garden_color,label=r'$N_a$')#alpha=0.5)
ax2.set_xlim(0,30)
ax2.set_ylim(0,1)
ax2.set(ylabel=r'$P(N^{(stable)})$',xlabel=r'$L$')

data1 = []
error1 = []
data2 = []
error2 = []
l1 = []
counter = 0
for vec in raw_data1.items():
  N = len(vec[1])
  data1.append(sum(vec[1])/N)
  l1.append(vec[0])
  dev = []
  for num in vec[1]:
    dev.append((num-data1[counter])*(num-data1[counter]))
  error1.append(np.sqrt(sum(dev)/N))
  counter+=1


l2 = []
counter = 0
for vec in other_data1.items():
  N = len(vec[1])
  data2.append(sum(vec[1])/N)
  l2.append(vec[0])
  dev = []
  for num in vec[1]:
    dev.append((num-data2[counter])*(num-data2[counter]))
  error2.append(np.sqrt(sum(dev)/N))
  counter+=1 

l1, data1 = zip(*sorted(zip(l1, data1)))
l2, data2 = zip(*sorted(zip(l2, data2)))

ax3.plot(l1,data1,color=basin_color,label=r'$N_f$')#alpha=0.5)
ax3.plot(l2,data2,color=garden_color,label=r'$N_a$')#alpha=0.5)
ax3.set_xlim(0,30)
ax3.set_ylim(0,1)
ax3.set(ylabel=r'$P(N_x)$',xlabel=r'$L$')
# ~ ax2.legend(loc=4)
#-----------------------------------------------------------------------
ax1 = plt.subplot(gs[0,2])
ax2 = plt.subplot(gs[1,2])
ax3 = plt.subplot(gs[2,2])


if gridbool:
    ax1.grid(True)
    ax2.grid(True)
    ax3.grid(True)

if setticks:
    ax1.set_xticks([0,10,20,30,40,50])
    ax2.set_xticks([0,10,20,30,40,50])
    ax3.set_xticks([0,10,20,30,40,50])

N = 1000000
data = []
with open("basin_of_attraction_master_N12_K_12.dat") as fobj:
    counter = 0
    for line in fobj:
        data.append([float(i) for i in line.split(' ') if not i == '\n'])
        counter += 1
        if counter == N: break
    #data = [[float(num) for num in line.split()] for line in fobj]


raw_data = defaultdict(list)
other_data = defaultdict(list)

for vec in data:
  if vec[2] > 1:
    if vec[4] > 0:
      raw_data[int(vec[2])].append(float(vec[5])/(vec[3]*vec[4]))
    if vec[7] > 0:
      other_data[int(vec[2])].append(float(vec[8])/(vec[3]*vec[7]))
      
data1 = []
error1 = []
data2 = []
error2 = []
l1 = []
counter = 0
for vec in raw_data.items():
  N = len(vec[1])
  data1.append(sum(vec[1])/N)
  l1.append(vec[0])
  dev = []
  for num in vec[1]:
    dev.append((num-data1[counter])*(num-data1[counter]))
  error1.append(np.sqrt(sum(dev)/N))
  counter+=1


l2 = []
counter = 0
for vec in other_data.items():
  N = len(vec[1])
  data2.append(sum(vec[1])/N)
  l2.append(vec[0])
  dev = []
  for num in vec[1]:
    dev.append((num-data2[counter])*(num-data2[counter]))
  error2.append(np.sqrt(sum(dev)/N))
  counter+=1 

l1, data1 = zip(*sorted(zip(l1, data1)))
l2, data2 = zip(*sorted(zip(l2, data2)))

ax1.set_title(r'$N=12, K=12$')
ax1.plot(l1,data1,color=basin_color,label=r'$N_f$')#alpha=0.5)
ax1.plot(l2,data2,color=garden_color,label=r'$N_a$')#alpha=0.5)
ax1.set_xlim(0,30)
ax1.set_ylim(0,1)
ax1.set(ylabel=r'$P(N^{(stable)})$',xlabel='$N_A$')
# ~ ax1.legend(loc=4)

#0NODES, 1DEGREE, 2number_attractors, 3length, 4num_frozen, 5frozen_stable, 6frozen_unstable, 7num_nonfrozen, 8nonfrozen_stable, 9nonfrozen_unstable, 10basin_of_attraction, 11garden_of_eden});

raw_data = defaultdict(list)
other_data = defaultdict(list)
raw_data1 = defaultdict(list)
other_data1 = defaultdict(list)

for vec in data:
  if vec[2] > 1 and vec[3] > 1:
    if vec[4] > 0:
      raw_data[int(vec[3])].append(float(vec[5])/(vec[3]*vec[4]))
    if vec[7] > 0:
      other_data[int(vec[3])].append(float(vec[8])/(vec[3]*vec[7]))
    raw_data1[int(vec[3])].append(float(vec[4])/vec[0])
    other_data1[int(vec[3])].append(float(vec[7])/vec[0])
    
data1 = []
error1 = []
data2 = []
error2 = []
l1 = []
counter = 0
for vec in raw_data.items():
  N = len(vec[1])
  data1.append(sum(vec[1])/N)
  l1.append(vec[0])
  dev = []
  for num in vec[1]:
    dev.append((num-data1[counter])*(num-data1[counter]))
  error1.append(np.sqrt(sum(dev)/N))
  counter+=1


l2 = []
counter = 0
for vec in other_data.items():
  N = len(vec[1])
  data2.append(sum(vec[1])/N)
  l2.append(vec[0])
  dev = []
  for num in vec[1]:
    dev.append((num-data2[counter])*(num-data2[counter]))
  error2.append(np.sqrt(sum(dev)/N))
  counter+=1

l1, data1 = zip(*sorted(zip(l1, data1)))
l2, data2 = zip(*sorted(zip(l2, data2)))

ax2.plot(l1,data1,color=basin_color,label=r'$N_f$')#alpha=0.5)
ax2.plot(l2,data2,color=garden_color,label=r'$N_a$')#alpha=0.5)
ax2.set_xlim(0,30)
ax2.set_ylim(0,1)
ax2.set(ylabel=r'$P(N^{(stable)})$',xlabel=r'$L$')

data1 = []
error1 = []
data2 = []
error2 = []
l1 = []
counter = 0
for vec in raw_data1.items():
  N = len(vec[1])
  data1.append(sum(vec[1])/N)
  l1.append(vec[0])
  dev = []
  for num in vec[1]:
    dev.append((num-data1[counter])*(num-data1[counter]))
  error1.append(np.sqrt(sum(dev)/N))
  counter+=1


l2 = []
counter = 0
for vec in other_data1.items():
  N = len(vec[1])
  data2.append(sum(vec[1])/N)
  l2.append(vec[0])
  dev = []
  for num in vec[1]:
    dev.append((num-data2[counter])*(num-data2[counter]))
  error2.append(np.sqrt(sum(dev)/N))
  counter+=1 

l1, data1 = zip(*sorted(zip(l1, data1)))
l2, data2 = zip(*sorted(zip(l2, data2)))

ax3.plot(l1,data1,color=basin_color,label=r'$N_f$')#alpha=0.5)
ax3.plot(l2,data2,color=garden_color,label=r'$N_a$')#alpha=0.5)
ax3.set_xlim(0,30)
ax3.set_ylim(0,1)
ax3.set(ylabel=r'$P(N_x)$',xlabel=r'$L$')
X = np.arange(2,19,0.1)
Y = 1/X
ax1.plot(X,Y,'g',ls='--',label=r'$1/N_A$')
ax1.legend(loc=1)
#-----------------------------------------------------------------------

plt.tight_layout()
plt.show()
# ~ fig.savefig("Basin_N"+text+".pdf")
