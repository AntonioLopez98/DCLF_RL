# Reinforcement-Learning-with-CLF-s
[![License](https://img.shields.io/badge/license-MIT-blue)](https://opensource.org/licenses/MIT)

This project contains code for some RL implementations where a Control Lyapunov Function is added on the reward function to accelerate the training process. This project also contains MATLAB code for computing Control Lyapunov Functions using Hamilton-Jacobi Reachability analysis. Read the full paper here. 



## Paper Abstract

A significant challenge in reinforcement learning (RL) algorithms is that they suffer from high sample complexity, translating into long computation times. This study introduces a fusion of control theory and RL to find policies of autonomous systems with relatively few training episodes. Leveraging Hamilton-Jacobi Reachability, we compute a Decomposed Control Lyapunov Function (DCLF) that encapsulates system stability and uses it as part of the reward function in RL, which we show improves RL performance. We also extend prior work by constructing Lyapunov functions for high-dimensional systems, mitigating the curse of dimensionality on a particular class of dynamical systems. Through multiple examples, including a 12-dimensional drone, we demonstrate the effectiveness of this approach, where we learned a policy faster and with less data than standard RL algorithms. 


## Dependencies 
- gym - 0.18.0 
- numpy - 1.19.5 
- matplotlib - 3.3.4 
- pytorch - 1.8.1 


### Constructing CLF

