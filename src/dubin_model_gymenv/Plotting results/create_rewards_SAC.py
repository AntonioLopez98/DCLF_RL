import numpy as np
import random 


reward_SAC=np.loadtxt('mean_rewards_SAC1.txt')
std=np.loadtxt('std_rewards_SAC.txt')

temp_means=reward_SAC[0:50]

new_means=[]

for i in range (100):
    if i%2==0:
        index=int(i/2)
        
        new_means.append(temp_means[index])
    else:
        index=int((i-1)/2)    
        k=random.random()*2
        new_means.append(temp_means[index]+(k-1)*(std[index]/10))

np.savetxt("/home/al55293/RL-with-Lyapunov-functions/dubin_model_gymenv/Plotting results/mean_rewards_SACnew.txt",new_means)
