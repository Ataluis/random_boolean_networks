import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from collections import defaultdict
from itertools import islice
from scipy.stats import pearsonr
import statsmodels.api as sm

#plot settings
params = {
    'text.usetex'       : True,
    'font.size'         : 18
}
matplotlib.rcParams.update(params)


filename = 'basin_of_attraction_master_N10_K_2.dat'

number = 20000

L1 = np.zeros((number,12))

counter = 0

with open(filename) as f:
  for line in f:
    L1[counter] = np.array([float(num) for num in line.split()])
    counter += 1
    if counter >= number : break

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
plt.plot(X_plot,Y_plot,'--g',label=r'$1/N_A = \mathcal{N}_B/\Omega$')

plt.scatter(data3[:5000],data4[:5000],color='black',marker='x',alpha=0.1)
plt.scatter(data2[:50],data[:50],color='orange',label = r'$\langle \mathcal{N}_B/\Omega\rangle_{N_A}$')#,label=r'$1/N_A$')
# ~ plt.scatter(range(1,len(data2)+1),data2,color='red',alpha=0.7,label=r'$N_B/\Omega$')
# ~ plt.plot(range(1,len(dist)+1),dist,'--g',label=r'$\textrm{Difference}$')

plt.grid(True)
plt.ylabel(r'$\mathcal{N}_B/\Omega$',fontsize=22)
plt.xlabel(r'$1/N_A$',fontsize=22)
#plt.ylabel(r'$1/N_A$',fontsize=18)
plt.xlim(0.0,1.0)
plt.ylim(0.0,1.0)
# ~ plt.legend(fontsize=18)
plt.subplots_adjust(top=.95,right=.95,left=.14,bottom=.14)
# ~ props = dict(boxstyle='round', facecolor='white', alpha=0.7)
# place a text box in upper left in axes coords
# ~ plt.text(0.05, 0.95, textstr, fontsize=18,
        # ~ verticalalignment='top', bbox=props)
plt.legend()
plt.show()
