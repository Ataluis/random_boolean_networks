import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from numpy import *
from collections import defaultdict
import matplotlib.gridspec as gridspec
from scipy.stats import pearsonr
import statsmodels.api as sm

#plot settings
params = {
    'text.usetex'       : True,
    'font.size'         : 16,
}
matplotlib.rcParams.update(params)

fig = plt.figure(figsize=(12,5.5))
gs = gridspec.GridSpec(1, 2)
#-----------------------------------------------------------------------
ax1 = plt.subplot(gs[0,0])
ax2 = plt.subplot(gs[0,1])

L1 = []

Length = 4.

end = 10000000
ALPHA = 0.5
Degree = 10
Omega = np.power(2,Degree)

counter = 0
with open('basin_of_attraction_master_N10_K_2.dat') as f:
  for line in f:
    vec = [float(num) for num in line.split()]
    for val in vec:
      val = float(val)
    L1.append(vec)
    if (L1[-1][3]) != (Length) : 
      del L1[-1]
      counter -= 1
    counter += 1
    if counter >= end:
      break

data = defaultdict(list)

for vec in L1:
  data[int(vec[2]-1)].append(vec[10]/float(np.power(2,10)))

results = np.zeros((3,len(data)))

counter = 0
for k,v in data.iteritems():
  results[0][counter] = k+1
  results[1][counter] = sum(v)/len(v)
  results[2][counter] = len(v)
  counter += 1

ax1.scatter(results[0], results[1],color='r',label=r'$L=4$',alpha=ALPHA)

Length = 5.

counter = 0
with open('basin_of_attraction_master_N10_K_2.dat') as f:
  for line in f:
    vec = [float(num) for num in line.split()]
    for val in vec:
      val = float(val)
    L1.append(vec)
    if (L1[-1][3]) != (Length) : 
      del L1[-1]
      counter -= 1
    counter += 1
    if counter >= end:
      break

data = defaultdict(list)

for vec in L1:
  data[int(vec[2]-1)].append(vec[10]/float(np.power(2,10)))

results = np.zeros((3,len(data)))

counter = 0
for k,v in data.iteritems():
  results[0][counter] = k+1
  results[1][counter] = sum(v)/len(v)
  results[2][counter] = len(v)
  counter += 1

ax1.scatter(results[0], results[1],color='b',label=r'$L=5$',alpha=ALPHA)

Length = 6.

counter = 0
with open('basin_of_attraction_master_N10_K_2.dat') as f:
  for line in f:
    vec = [float(num) for num in line.split()]
    for val in vec:
      val = float(val)
    L1.append(vec)
    if (L1[-1][3]) != (Length) : 
      del L1[-1]
      counter -= 1
    counter += 1
    if counter >= end:
      break

data = defaultdict(list)

for vec in L1:
  data[int(vec[2]-1)].append(vec[10]/float(np.power(2,10)))

results = np.zeros((3,len(data)))

counter = 0
for k,v in data.iteritems():
  results[0][counter] = k+1
  results[1][counter] = sum(v)/len(v)
  results[2][counter] = len(v)
  counter += 1

ax1.scatter(results[0], results[1],color='g',label=r'$L=6$',alpha=ALPHA)

# ~ for i, txt in enumerate(results[2]):
  # ~ if i < 4:
    # ~ ax.annotate(str(int(txt)), (results[0][i], results[1][i]))
  # ~ elif i%2 == 1:
    # ~ ax.annotate(str(int(txt)), (results[0][i], results[1][i]),)

x = np.arange(1.0,23.0,0.1)
f = 1./x
ax1.plot(x,f,'--',color='grey',label=r'$1/N_A$')
ax1.grid(True)
ax1.set_title(r'$N=10, K=2$')
ax1.set_xlim((-0.5,21.5))
ax1.set_xlabel(r'$N_A$',fontsize=22)
ax1.set_ylabel(r'$\mathcal{N}_B/\Omega$',fontsize=22)
ax1.legend(loc=1)


filename = 'basin_of_attraction_master_N10_K_2.dat'

number = 20000000

L1 = np.zeros((number,12))

counter = 0

with open(filename) as f:
  for line in f:
    L1[counter] = np.array([float(num) for num in line.split()])
    counter += 1
    if counter >= number : break

#run N K p L 5NB/Omega10 6N_Att_in_this_run2 garden_of_eden_states/Omega

raw_data = defaultdict(list)
raw_data2 = defaultdict(list)

data3 = []
data4 = []

counter = 0
for vec in L1:
  raw_data[int(vec[2])].append(vec[2])
  raw_data2[int(vec[2])].append(vec[10]/float(np.power(2,10)))
  data3.append(1./vec[2])
  data4.append(vec[10]/float(np.power(2,10)))
  counter += 1

data = []
data2 = []

for vec in raw_data.items():
  N = len(vec[1])
  data.append(1./(sum(vec[1])/N))
  
for vec in raw_data2.items():
  N = len(vec[1])
  data2.append((sum(vec[1])/N))

dist = []

for i in range(0,len(data)):
  if(data2[i]-data[i]!=0.):
    dist.append((data2[i]-data[i]))

corr, _ = pearsonr(data2[:50],data[:50])

mod = sm.OLS(data2[:50],data[:50])
results = mod.fit()

# ~ textstr = '\n'.join((

    # ~ r'$Fit(N_B/\Omega)=\alpha \cdot N_B/\Omega $',
    # ~ r'$\alpha=%.3f\pm %.3f$' % (1./results.params[0], results.bse[0], ),
    # ~ r'$corr=%.3f$' % (corr)))

X_plot = np.linspace(0.,1.,1000)
Y_plot = (1./results.params[0])*X_plot
ax2.plot(X_plot,Y_plot,'--g',label=r'$1/N_A = \mathcal{N}_B/\Omega$')

ax2.scatter(data3[:5000],data4[:5000],color='black',marker='x',alpha=0.1)
ax2.scatter(data2[:50],data[:50],color='orange',label = r'$\langle \mathcal{N}_B/\Omega\rangle_{N_A}$')#,label=r'$1/N_A$')
# ~ plt.scatter(range(1,len(data2)+1),data2,color='red',alpha=0.7,label=r'$N_B/\Omega$')
# ~ plt.plot(range(1,len(dist)+1),dist,'--g',label=r'$\textrm{Difference}$')

ax2.grid(True)
ax2.set_title(r'$N=10, K=2$')
ax2.set_ylabel(r'$\mathcal{N}_B/\Omega$',fontsize=22)
ax2.set_xlabel(r'$1/N_A$',fontsize=22)
#plt.ylabel(r'$1/N_A$',fontsize=18)
ax2.set_xlim(0.0,1.0)
ax2.set_ylim(0.0,1.0)
# ~ plt.legend(fontsize=18)

# ~ props = dict(boxstyle='round', facecolor='white', alpha=0.7)
# place a text box in upper left in axes coords
# ~ plt.text(0.05, 0.95, textstr, fontsize=18,
        # ~ verticalalignment='top', bbox=props)
ax2.legend()




plt.tight_layout()

plt.show()
#~ plt.savefig('const_length_critical.pdf')
