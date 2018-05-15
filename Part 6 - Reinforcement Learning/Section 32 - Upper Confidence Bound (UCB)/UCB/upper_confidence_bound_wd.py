import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math
# Importing the dataset
dataset = pd.read_csv('Ads_CTR_Optimisation.csv')

#Implementing the UCB(from scratch.!!)
#we need to consider this number for each ad i. We're going to create a vector that will contain each of those members of selections of each ad i. So we will set this variable to vector of size d and we will initialize all components of this vector to zero.
d=10 
numbers_of_selections=[0]*d

#This will create a vector of size d with zeros in it and we are doing this because of course at first round each version of the ad isn't being selected at,so no of times each version of the ad gets selected is of cousre 0
N=10000

ads_selected=[]
#sum of rewards of ad i upto round n, so we are going to set it as vector of decomponentsN=10000
sums_of_rewards=[0]*d
total_reward=0
for n in range(0, N):
    ad = 0
    max_upper_bound = 0
    for i in range(0, d):
        if (numbers_of_selections[i] > 0):
            average_reward = sums_of_rewards[i] / numbers_of_selections[i]
            delta_i = math.sqrt(3/2 * math.log(n + 1) / numbers_of_selections[i])
            upper_bound = average_reward + delta_i
        else:
            upper_bound = 1e400
        if upper_bound > max_upper_bound:
            max_upper_bound = upper_bound
            ad = i
    ads_selected.append(ad)
    numbers_of_selections[ad] = numbers_of_selections[ad] + 1
    reward = dataset.values[n, ad]
    sums_of_rewards[ad] = sums_of_rewards[ad] + reward
    total_reward = total_reward + reward

#Visualising The Results
plt.hist(ads_selected)
plt.title('Hostogram: ADS Selections')
plt.xlabel("Ads")
plt.ylabel('No of Times Each add was selected')
plt.show()
    
            
        
        
        
    


