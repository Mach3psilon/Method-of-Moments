# -*- coding: utf-8 -*-
"""


@author: Eray Okutay
"""
import numpy as np

import math
from matplotlib import pyplot as plt

def distribute_binomialy(number_of_trials,probability,sample_size):
    N = number_of_trials
    p = probability
    Y = []
    for j in range(sample_size):
        X = []
        for i in range(N):
            u = np.random.rand()
            x = u<p
            X.append(x)
        y = sum(X)
        Y.append(y)
    return Y



def calculate_mean(numbers):
    sumof = 0 
    for i in numbers:
        sumof += i
    return sumof/len(numbers)


def calculate_standart_deviation(numbers):
    mean = calculate_mean(numbers)
    sum_of_subtracktions = 0 
    for i in numbers:
        subtracked = i-mean
        sum_of_subtracktions += (subtracked**2)
    return math.sqrt(sum_of_subtracktions/(len(numbers)))

def kth_sample_moment(k,numbers):

    sumof = 0
    for i in numbers:
        sumof += i**k
    return sumof/len(numbers)


def kth_central_sample_moment(k,numbers):
    mean = calculate_mean(numbers)
    sumof = 0
    for i in numbers:
        sumof += abs((i-mean))**k
    return sumof/len(numbers)

def lets_roll(trial_time,N):
    Y = []
    Z = []
    for i in range(trial_time):
        dist = distribute_binomialy(40,0.3,N)
        population_moment1 = kth_sample_moment(1,dist)
        central_moment2 = kth_central_sample_moment(2,dist)
        one_minus_p = central_moment2/population_moment1
        p = -(one_minus_p-1)
        n = population_moment1/p
        Y.append(p)
        Z.append(n)
      
    print("Mean for estimated p for sample size of",N,"is",calculate_mean(Y))
    print("Standart deviation for estimated p for sample size of",N,"is",calculate_standart_deviation(Y),"\n")
    print("Mean for estimated n for sample size of",N,"is",calculate_mean(Z))
    print("Standart deviation for estimated n for sample size of",N,"is",calculate_standart_deviation(Z),"\n")
    return Y,Z 

def main(trial_time):
    p_200,n_200 = lets_roll(trial_time,200)
    p_800,n_800 = lets_roll(trial_time,800)
    p_3200,n_3200 = lets_roll(trial_time,3200)
    kwargs = dict(alpha=0.5, bins=100)
    
    plt.hist(p_200, **kwargs, color='#e2979c', label='200')
    plt.hist(p_800, **kwargs, color='#4cd3c2', label='800')
    plt.hist(p_3200, **kwargs, color='#d92027', label='3200')
    plt.gca().set(title='Histogram for estimated p')
    
    plt.show()
    plt.figure()
    
    
    plt.hist(n_200, **kwargs, color='#e2979c', label='200')
    plt.hist(n_800, **kwargs, color='#4cd3c2', label='800')
    plt.hist(n_3200, **kwargs, color='#d92027', label='3200')
    plt.gca().set(title='Histogram for estimated n')
    plt.show()
    
print("Plotting the histograms may take a while.\n")
main(1000)
    
   
    
    


















