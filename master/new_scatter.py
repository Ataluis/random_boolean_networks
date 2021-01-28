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



filename = 'basin_of_attraction_master_N10_K_1_5.dat'

number = 10000000

L1 = np.zeros((number,12))

counter = 0

with open(filename) as f:
  for line in f:
    L1[counter] = np.array([float(num) for num in line.split()])
    counter += 1
    if counter >= number : break


#L1 = [[float(num) for num in line.split()] for line in f] #run N K p L NB/Omega N_Att_in_this_run garden_of_eden_states/Omega

raw_data = [defaultdict(list),defaultdict(list),defaultdict(list),defaultdict(list),defaultdict(list),
defaultdict(list),defaultdict(list),defaultdict(list),defaultdict(list),defaultdict(list)]
Length = []

counter = 0
for vec in L1:
  raw_data[int(np.floor(counter/(number/10.)))][int(vec[3])].append(vec[10]/float(np.power(2,vec[0])))
  counter += 1
  if int(vec[3]) not in Length:
    Length.append(int(vec[3]))

Length.sort()

to_mean = []
val = 17

for i in range(0,10):
  data = []
  error = []

  counter = 0
  for vec in raw_data[i].items():
    N = len(vec[1])
    data.append(sum(vec[1])/N)
    dev = []
    for num in vec[1]:
      dev.append((num-data[counter])*(num-data[counter]))
    error.append(np.sqrt(sum(dev)/N))
    counter+=1 
  to_mean.append(data)
  ax1.scatter(Length[:val],data[:val],marker='x',alpha=0.7)

mean = []
error = []

to_mean = zip(*to_mean)
counter = 0
for vec in to_mean:
  mean.append(sum(vec)/10.)
  dev = []
  for i in range(0,10):
    dev.append((vec[i]-mean[counter])*(vec[i]-mean[counter]))
  error.append(np.sqrt(sum(dev)/10.))
  counter += 1

ax1.scatter(Length[:val],mean[:val],marker='o',color='r',label=r'$\langle N_B/\Omega \rangle_{2\cdot10^7}$')
ax1.errorbar(Length[:val],mean[:val],error[:val],fmt='none',color='r')

ax1.grid(True)
ax1.set_xlabel(r'$L$')
ax1.set_ylabel(r'$\mathcal{N}_B/\Omega$')
ax1.set_title(r'$N=10, K=1.5$')
ax1.set_xticks([3,6,9,12,15])
ax1.set_xlim(0.5,17.5)
#############################################################################
#############################################################################
number = 20000000
filename = 'basin_of_attraction_master_N10_K_2.dat'

L1 = np.zeros((number,12))

counter = 0

with open(filename) as f:
  for line in f:
    L1[counter] = np.array([float(num) for num in line.split()])
    counter += 1
    if counter >= number : break

#L1 = [[float(num) for num in line.split()] for line in f] #run N K p L NB/Omega N_Att_in_this_run garden_of_eden_states/Omega

raw_data = [defaultdict(list),defaultdict(list),defaultdict(list),defaultdict(list),defaultdict(list),
defaultdict(list),defaultdict(list),defaultdict(list),defaultdict(list),defaultdict(list)]

counter = 0
for vec in L1:
  raw_data[int(np.floor(counter/(number/10.)))][int(vec[3])].append(vec[10]/float(np.power(2,vec[0])))
  counter += 1

to_mean = []

for i in range(0,10):
  data = []
  error = []

  counter = 0
  for vec in raw_data[i].items():
    N = len(vec[1])
    data.append(sum(vec[1])/N)
    dev = []
    for num in vec[1]:
      dev.append((num-data[counter])*(num-data[counter]))
    error.append(np.sqrt(sum(dev)/N))
    counter+=1 
  to_mean.append(data)
  ax2.scatter(range(1,len(data)+1),data,marker='x',alpha=0.7)

mean = []
error = []

to_mean = zip(*to_mean)
counter = 0
for vec in to_mean:
  mean.append(sum(vec)/10.)
  dev = []
  for i in range(0,10):
    dev.append((vec[i]-mean[counter])*(vec[i]-mean[counter]))
  error.append(np.sqrt(sum(dev)/10.))
  counter += 1

ax2.scatter(range(1,len(mean)+1),mean,marker='o',color='r',label=r'$\langle N_B/\Omega \rangle_{2\cdot10^7}$')
ax2.errorbar(range(1,len(mean)+1),mean,error,fmt='none',color='r')

ax2.grid(True)
ax2.set_xlabel(r'$L$')
ax2.set_ylabel(r'$\mathcal{N}_B/\Omega$')
ax2.set_title(r'$N=10, K=2$')
ax2.set_xlim(0.5,25.5)
#plt.legend(scatteryoffsets=[0.5])
plt.tight_layout()
plt.show()
