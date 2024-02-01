import numpy as np
import matplotlib.pyplot as plt


reward_CLVF=np.loadtxt('mean_rewards_sys_SAC.txt')*4
std_CLVF=np.loadtxt("std_rewards_sys_SAC.txt")

reward_CLVF_full=np.loadtxt('mean_rewards_full_SAC.txt')*4
std_CLVF_full=np.loadtxt('std_rewards_full_SAC.txt')

reward_SAC=np.loadtxt('mean_rewards_SACnew.txt')*4
std_SAC=np.loadtxt('std_rewards_SAC.txt')

t=np.arange(len(reward_CLVF))
n=len(reward_CLVF)
fig, ax = plt.subplots(1)

ax.plot(t, reward_CLVF[0:n], lw=2, label='CLVF_SAC', color='teal')
ax.fill_between(t, reward_CLVF[0:n]+std_CLVF[0:n], reward_CLVF[0:n]-std_CLVF[0:n], facecolor='cadetblue', alpha=0.5)

ax.plot(t, reward_CLVF_full[0:n], lw=2, label='DCLF_SAC', color='orange')
ax.fill_between(t, reward_CLVF_full[0:n]+std_CLVF_full[0:n], reward_CLVF_full[0:n]-std_CLVF_full[0:n], facecolor='orange', alpha=0.5)

ax.plot(t, reward_SAC[0:n], lw=2, label='SAC baseline', color='salmon')
ax.fill_between(t, reward_SAC[0:n]+std_SAC[0:n], reward_SAC[0:n]-std_SAC[0:n], facecolor='lightsalmon', alpha=0.5)

#ax.set_title('Dubins Car reward for different RL algorithms')
ax.legend(loc='lower right')
ax.set_xlabel('Epoch')
ax.set_ylabel('Reward')
#ax.grid()
plt.show()
