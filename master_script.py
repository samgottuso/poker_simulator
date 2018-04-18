# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 14:13:16 2018

@author: 583185
"""
#Imports
import numpy as np


#Playing  with normal logic, each one simulates 100 hands, so we get 20 players playing 100 hands

from play_hand import play_hand

r1=play_hand(players=5,starting_money=200,hands=100,table_min=5)

r2=play_hand(players=5,starting_money=200,hands=100,table_min=5)

r3=play_hand(players=5,starting_money=200,hands=100,table_min=5)

r4=play_hand(players=5,starting_money=200,hands=100,table_min=5)

normal_values=np.array(list(r1.values())+list(r2.values())+list(r3.values())+list(r4.values()))
mean_normal_values=np.mean(normal_values)
std_normal_values=np.std(normal_values)


#Second Model

#Playing  with alt logic, each one simulates 100 hands, so we get 20 players playing 100 hands


from play_hand_inside import play_hand_inside

r5=play_hand_inside(players=5,starting_money=200,hands=100,table_min=5)

r6=play_hand_inside(players=5,starting_money=200,hands=100,table_min=5)

r7=play_hand_inside(players=5,starting_money=200,hands=100,table_min=5)

r8=play_hand_inside(players=5,starting_money=200,hands=100,table_min=5)

alt_values=np.array(list(r5.values())+list(r6.values())+list(r7.values())+list(r8.values()))
mean_alt_values=np.mean(alt_values)
std_alt_values=np.std(alt_values)

from scipy import stats
#hand t stat
t_stat=(mean_alt_values-.48)/((std_alt_values)/np.sqrt(len(alt_values)))


#scipy t stat-- not entirely sure this is appropriate
tval=stats.ttest_ind(normal_values,alt_values)
print(tval)