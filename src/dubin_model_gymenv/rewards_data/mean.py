import numpy as np
import statistics

n=95 #number of trainings 
k=112 #minimum number of episodes in a training process
trainings_list=[]

for i in range (24,n):
    filename='rewards_full_SAC/reward_CLVF_full_SAC'+str(i)+'.txt'
    new_training=np.loadtxt(filename)
    trainings_list.append(new_training[0:k])



means=[]

std_devs=[]

for i in range (k):
    temp_mean=0
    std_list=[]
    for j in range (n-24):
        temp_mean+=trainings_list[j][i]
        std_list.append(trainings_list[j][i])
    
    sigma=statistics.pstdev(std_list)
    temp_mean=temp_mean/(n-24)
    means.append(temp_mean)
    std_devs.append(sigma)

print(means)

np.savetxt("/home/al55293/RL-with-Lyapunov-functions/dubin_model_gymenv/Plotting results/mean_rewards_full_SAC.txt",means)
np.savetxt("/home/al55293/RL-with-Lyapunov-functions/dubin_model_gymenv/Plotting results/std_rewards_full_SAC.txt",std_devs)