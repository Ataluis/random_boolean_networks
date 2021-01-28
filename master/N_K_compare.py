import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from collections import defaultdict
from itertools import islice
import matplotlib.gridspec as gridspec

#plot settings
params = {
    'text.usetex'       : True,
    'font.size'         : 16
}
matplotlib.rcParams.update(params)
fig = plt.figure(figsize=(12,6))
gs = gridspec.GridSpec(1, 2)
ax1 = plt.subplot(gs[0,0])
ax2 = plt.subplot(gs[0,1])

L1 = []

counter = 0

with open('basin_of_attraction_master_N10_K_10.dat') as f:
  for line in f:
    L1.append([float(num) for num in line.split()])
    counter += 1
    if counter > 20000000:
      break

#L1 = [[float(num) for num in line.split()] for line in f] #run N K p L NB/Omega N_Att_in_this_run garden_of_eden_states/Omega

raw_data = defaultdict(list)

for vec in L1:
  raw_data[vec[3]].append(vec[10]/(np.power(2,vec[0])))

data = []
error = []

counter = 0
for vec in raw_data.items():
  N = len(vec[1])
  data.append(sum(vec[1])/N)
  dev = []
  for num in vec[1]:
    dev.append((num-data[counter])*(num-data[counter]))
  error.append(np.sqrt(sum(dev)/N))
  counter+=1 

L = np.arange(1,len(data)+1)/np.sqrt(2*float(np.power(2,10)))
ax1.scatter(range(1,len(data)+1),data,color='r',label=r'$N=10$',alpha=0.5,marker='1')
ax2.plot(L,data,color='r',label=r'$N=10$')

counter = 0

with open('basin_of_attraction_master_N12_K_12.dat') as f:
  for line in f:
    L1.append([float(num) for num in line.split()])
    counter += 1
    if counter > 20000000:
      break

#L1 = [[float(num) for num in line.split()] for line in f] #run N K p L NB/Omega N_Att_in_this_run garden_of_eden_states/Omega

raw_data = defaultdict(list)

for vec in L1:
  raw_data[vec[3]].append(vec[10]/(np.power(2,vec[0])))

data = []
error = []

counter = 0
for vec in raw_data.items():
  N = len(vec[1])
  data.append(sum(vec[1])/N)
  dev = []
  for num in vec[1]:
    dev.append((num-data[counter])*(num-data[counter]))
  error.append(np.sqrt(sum(dev)/N))
  counter+=1 

L = np.array(range(1,len(data)+1))/np.sqrt(2*float(np.power(2,12)))
ax1.scatter(range(1,len(data)+1),data,color='g',label=r'$N=12$',alpha=0.5,marker='2')
ax2.plot(L,data,color='g',label=r'$N=12$')

counter = 0

with open('basin_of_attraction_master_N14_K_14.dat') as f:
  for line in f:
    L1.append([float(num) for num in line.split()])
    counter += 1
    if counter > 20000000:
      break

#L1 = [[float(num) for num in line.split()] for line in f] #run N K p L NB/Omega N_Att_in_this_run garden_of_eden_states/Omega

raw_data = defaultdict(list)

for vec in L1:
  raw_data[vec[3]].append(vec[10]/(np.power(2,vec[0])))


data = []
error = []

counter = 0
for vec in raw_data.items():
  N = len(vec[1])
  data.append(sum(vec[1])/N)
  dev = []
  for num in vec[1]:
    dev.append((num-data[counter])*(num-data[counter]))
  error.append(np.sqrt(sum(dev)/N))
  counter+=1 

L = np.array(range(1,len(data)+1))/np.sqrt(2*float(np.power(2,14)))
ax1.scatter(range(1,len(data)+1),data,color='b',label=r'$N=14$',alpha=0.5,marker='+')
ax2.plot(L,data,color='b',label=r'$N=14$')

ax1.grid(True)
ax1.set_xlabel(r'$L$')
ax1.set_ylabel(r'$\mathcal{N_B}/\Omega$')
ax1.legend(loc=4)

ax2.grid(True)
ax2.set_xlabel(r'$L/\sqrt{2\Omega}$')
ax2.set_ylabel(r'$\mathcal{N_B}/\Omega$')
ax2.legend(loc=4)

plt.tight_layout()
plt.show()
