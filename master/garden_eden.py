import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import math
from collections import defaultdict

#plot settings
plt.rcParams.update({
    "text.usetex": True,
    "font.size" : 16
})

#Grid
fig = plt.figure(figsize=(7,7))


gs = gridspec.GridSpec(1,1)#2, 3, height_ratios=[1.5,1])
#-----------------------------------------------------------------------
ax1 = plt.subplot(gs[0])#0,0])
#~  ax2 = plt.subplot(gs[1,0])

#phase_space = np.power(2,12)


N = 10000000
data = []
with open("basin_of_attraction_master_N8_K_8.dat") as fobj:
    counter = 0
    for line in fobj:
        data.append([float(i) for i in line.split(' ') if not i == '\n'])
        counter += 1
        if counter == N: break
    
    
garden_eden = 0.0

elements = []

num_elements = 0
for vec in data:
    elements.append(float(vec[11])/vec[10])

print(np.mean(elements))
print(np.std(elements))


