import matplotlib.pyplot as plt
import numpy as np

sac=[0,0,0,0,0,0,0,0,0,0,
     0,1,1,1,1,1,1,1,1,2,
     2,3,3,3,3,4,4,5,5,5,
     5,5,5,5,5,5,5,5,6,6,
     6,6,7,7,7,7,7,7,7,8,
     8,8,8,8,8,8,8,9,9,9,
     9,10,10,11,11,11,11,11,11,
     11,11,11,11,11,11,11,11,11,11,12,12
]

sys=[0,0,0,0,0,0,0,1,1,2,
     2,3,3,4,4,4,4,4,4,4,
     5,5,6,6,7,7,7,7,7,7,
     7,7,7,7,7,8,8,9,9,10,
     10,10,11,11,12,13,14,15,16,17,
     18,19,20,21,21,21,21,22,23,24,
     25,26,27,28,29,30,31,31,31,32,
     33,34,35,36,36,37,38,39,40,41,
     42
]

clvf=[0,0,0,0,0,0,0,0,0,0,
     0,0,0,0,0,0,0,1,1,1,
     1,2,2,2,3,3,3,3,3,4,4,
     5,6,7,8,9,10,10,11,11,12,
     13,14,15,16,17,18,19,20,21,21,22,
     29,30,31,31,31,32,33,34,35,36,36,37,38,
     39,40,40,40,41,42,43,44,45,46,47,
     47,48,49,50,50
]



     
t=np.arange(81)


fig, ax = plt.subplots(1)

ax.plot(t, sac, lw=2, label='SAC_baseline gamma=0.99', color='green')
ax.plot(t, clvf, lw=2, label='CLF gamma=0.8', color='blue')
ax.plot(t, sys, lw=2, label='CLF_sys gamma=0.8', color='red')


ax.set_title('Goals reached per algorithm')
ax.legend(loc='upper left')
ax.set_xlabel('Episode number')
ax.set_ylabel('Total goals reached')
ax.grid()
plt.show()