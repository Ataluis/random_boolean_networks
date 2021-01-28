import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from collections import defaultdict
from itertools import islice
import matplotlib.gridspec as gridspec
from scipy import signal


#plot settings
params = {
    'text.usetex'       : True,
    'font.size'         : 16
}
matplotlib.rcParams.update(params)
fig = plt.figure(figsize=(12,4.5))
gs = gridspec.GridSpec(1, 3)
ax1 = plt.subplot(gs[0,0])
ax2 = plt.subplot(gs[0,1])
ax3 = plt.subplot(gs[0,2])



filename = 'basin_of_attraction_master_N10_K_1_5.dat'

number = 100000

L1 = np.zeros((number,12))

counter = 0

with open(filename) as f:
  for line in f:
    L1[counter] = np.array([float(num) for num in line.split()])
    counter += 1
    if counter >= number : break

raw_data = defaultdict(list)
raw_data1 = defaultdict(list)
Length = []

counter = 0
for vec in L1:
  raw_data[int(vec[3])].append(vec[10]/float(np.power(2,vec[0])))
  raw_data1[int(vec[3])].append(vec[2])
  counter += 1
  if int(vec[3]) not in Length:
    Length.append(int(vec[3]))
    
basin = []
na = []

for key, vec in raw_data.items():
  basin.append(float(sum(vec))/len(vec))
  
for key, vec in raw_data1.items():
  na.append(len(vec)/float(sum(vec)))

Length.sort()

val = 25
ax1.plot(Length[:val],basin[:val],color='r',label=r'$\langle \mathcal{N}_B/\Omega \rangle$')
ax1.plot(Length[:val],na[:val],color='b',label=r'$\langle 1/N_A \rangle$')

proportion = []
for i in range(0,len(basin)):
  proportion.append(na[i]/basin[i])


ax1.plot(Length[:val],proportion[:val],color='g',ls='--',label=r'$\langle\Omega/(N_A \mathcal{N}_B) \rangle$')
corr = np.corrcoef(basin[:val], na[:val])
labelstring = r'$\mathrm{corr}(1/N_A, \mathcal{N}_B)='+('%.3f' % corr[1][0])+'$'
# ~ ax2.scatter([-1],[-1],color='white',alpha=0.0,label=labelstring)
ax1.text(0.05, 0.1, labelstring, transform=ax1.transAxes,
        verticalalignment='top')
ax1.grid(True)
ax1.set_xlabel(r'$L$')
# ~ ax1.set_ylabel(r'$\mathcal{N}_B/\Omega$')
ax1.set_title(r'$N=10, K=1.5$')
ax1.set_xticks([0,5,10,15,20])
ax1.legend()
ax1.set_xlim(0.5,20.5)
ax1.set_ylim(0.0,1.0)
#############################################################################
#############################################################################
filename = 'basin_of_attraction_master_N10_K_2.dat'

number = 100000

L1 = np.zeros((number,12))

counter = 0

with open(filename) as f:
  for line in f:
    L1[counter] = np.array([float(num) for num in line.split()])
    counter += 1
    if counter >= number : break

raw_data = defaultdict(list)
raw_data1 = defaultdict(list)
Length = []

counter = 0
for vec in L1:
  raw_data[int(vec[3])].append(vec[10]/float(np.power(2,vec[0])))
  raw_data1[int(vec[3])].append(vec[2])
  counter += 1
  if int(vec[3]) not in Length:
    Length.append(int(vec[3]))
    
basin = []
na = []

for key, vec in raw_data.items():
  basin.append(float(sum(vec))/len(vec))
  
for key, vec in raw_data1.items():
  na.append(len(vec)/float(sum(vec)))

Length.sort()

val = 25
ax2.plot(Length[:val],basin[:val],color='r',label=r'$\langle \mathcal{N}_B/\Omega \rangle$')
ax2.plot(Length[:val],na[:val],color='b',label=r'$\langle 1/N_A \rangle$')

proportion = []
for i in range(0,len(basin)):
  proportion.append(na[i]/basin[i])

ax2.plot(Length[:val],proportion[:val],color='g',ls='--',label=r'$\langle\Omega/(N_A \mathcal{N}_B) \rangle$')
corr = np.corrcoef(basin[:val], na[:val])
labelstring = r'$\mathrm{corr}(1/N_A, \mathcal{N}_B)='+('%.3f' % corr[1][0])+'$'
# ~ ax2.scatter([-1],[-1],color='white',alpha=0.0,label=labelstring)
ax2.text(0.05, 0.1, labelstring, transform=ax2.transAxes,
        verticalalignment='top')
ax2.grid(True)
ax2.set_xlabel(r'$L$')
# ~ ax2.set_ylabel(r'$\mathcal{N}_B/\Omega$')
ax2.set_title(r'$N=10, K=2$')
ax2.set_xticks([0,5,10,15,20])
ax2.legend()
ax2.set_xlim(0.5,20.5)
ax2.set_ylim(0.0,1.0)
#############################################################################
#############################################################################
filename = 'basin_of_attraction_master_N10_K_10.dat'

number = 100000

L1 = np.zeros((number,12))

counter = 0

with open(filename) as f:
  for line in f:
    L1[counter] = np.array([float(num) for num in line.split()])
    counter += 1
    if counter >= number : break

raw_data = defaultdict(list)
raw_data1 = defaultdict(list)
Length = []

counter = 0
for vec in L1:
  raw_data[int(vec[3])].append(vec[10]/float(np.power(2,vec[0])))
  raw_data1[int(vec[3])].append(vec[2])
  counter += 1
  if int(vec[3]) not in Length:
    Length.append(int(vec[3]))
    
basin = []
na = []

for key, vec in raw_data.items():
  basin.append(float(sum(vec))/len(vec))
  
for key, vec in raw_data1.items():
  na.append(len(vec)/float(sum(vec)))

Length.sort()

val = 50
ax3.plot(Length[:val],basin[:val],color='r',label=r'$\langle \mathcal{N}_B/\Omega \rangle$')
ax3.plot(Length[:val],na[:val],color='b',label=r'$\langle 1/N_A \rangle$')

proportion = []
for i in range(0,len(basin)):
  proportion.append(na[i]/basin[i])

ax3.plot(Length[:val],proportion[:val],color='g',ls='--',label=r'$\langle\Omega/(N_A \mathcal{N}_B) \rangle$')
corr = np.corrcoef(basin[:val], na[:val])
labelstring = r'$\mathrm{corr}(1/N_A, \mathcal{N}_B)='+('%.3f' % corr[1][0])+'$'
# ~ ax2.scatter([-1],[-1],color='white',alpha=0.0,label=labelstring)
ax3.text(0.05, 0.1, labelstring, transform=ax3.transAxes,
        verticalalignment='top')
ax3.grid(True)
ax3.set_xlabel(r'$L$')
ax3.set_ylabel(r'$\mathcal{N}_B/\Omega$')
ax3.set_title(r'$N=10, K=10$')
ax3.set_xticks([0,10,20,30,40,50])
ax3.legend()
ax3.set_xlim(0.5,50.5)
ax3.set_ylim(0.0,1.0)
#plt.legend(scatteryoffsets=[0.5])
plt.tight_layout()
plt.show()
