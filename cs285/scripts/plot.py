import numpy as np
import matplotlib.pyplot as plt
import pickle
import os

def dict2array(dict_):

    avg = [di['Eval_AverageReturn'] for di in dict_]
    std = [di['Eval_StdReturn'] for di in dict_]
    return avg, std

bc_ant_pth = '../../data/q1_bc_ant_Ant-v2_12-10-2020_18-40-45/return.pkl'
da_ant_pth = '../../data/q2_dagger_ant_Ant-v2_12-10-2020_18-41-38/return.pkl'

bc_walk_pth = '../../data/q1_bc_walker_Walker2d-v2_12-10-2020_18-40-35/return.pkl'
da_walk_pth = '../../data/q2_dagger_walker_Walker2d-v2_12-10-2020_18-40-18/return.pkl'

ant_data = []
walk_data = []
for pth in [bc_ant_pth,da_ant_pth]:
    f = open(pth,'rb')
    data = pickle.load(f)
    f.close()
    ant_data.append(data)

for pth in [bc_walk_pth,da_walk_pth]:
    f = open(pth,'rb')
    data = pickle.load(f)
    f.close()
    walk_data.append(data)

ex_ant = ([di['Expert_AverageReturn'] for di in ant_data[0]],
          [di['Expert_StdReturn'] for di in ant_data[0]])

bc_ant = dict2array(ant_data[0])
da_ant = dict2array(ant_data[1])
x = range(len(bc_ant[0]))
plt.errorbar(x,bc_ant[0],yerr=bc_ant[1],label='BC')
plt.errorbar(x,da_ant[0],yerr=da_ant[1],label='Dagger')
plt.errorbar(x,ex_ant[0],yerr=ex_ant[1],label='Expert')
plt.legend()
plt.title('Ant Performance')
plt.savefig('../../data/Ant_performance.png')
plt.close('all')

ex_walk = ([di['Expert_AverageReturn'] for di in walk_data[0]],
          [di['Expert_StdReturn'] for di in walk_data[0]])

bc_walk = dict2array(walk_data[0])
da_walk = dict2array(walk_data[1])
x = range(len(bc_walk[0]))

plt.errorbar(x,bc_walk[0],yerr=bc_walk[1],label='BC')
plt.errorbar(x,da_walk[0],yerr=da_walk[1],label='Dagger')
plt.errorbar(x,ex_walk[0],yerr=ex_walk[1],label='Expert')
plt.legend()
plt.title('Walker2d Performance')
plt.savefig('../../data/Walker2d_performance.png')

