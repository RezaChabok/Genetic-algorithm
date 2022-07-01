from math import cos, sqrt
import random
import matplotlib.pyplot as plt
import numpy as np
from sys import exit
flag = False
crms = []
x = 0
g_best = []  # gbest
p_best = []  # pbest
avg_fit_crm = []
xi_end = 600
pop = 200
generates = 1000
end = 20
x_save = []


def generate():
        global pop, xi_end, crms, avg_fit_crm, select, x_save, x
        crms = []
        x_save = []
        x_save.append(x)
        crms.append(select)
        a = 1.0000 / 4000
        avg = 0
        for i in range(pop - 1):
            xi = random.randrange(0, xi_end)
            sum = 0
            for j in range(1, 11):
                sum += (xi * xi)
            multi = cos(xi / sqrt(1)) + 1
            for j in range(2, 11):
                multi *= cos(xi / sqrt(j)) + 1
            result = (a * sum) - multi
            avg += result
            crms.append(result)
            x_save.append(xi)

        avg_fit_crm.append(avg / pop)
        print("Generated.")

def best_select():
        global crms, p_best, select, x, x_save
        crms_save = crms
        sorted_crms = sorted(crms_save)
        p_best.append(sorted_crms[0])
        select = sorted_crms[0]
        index = crms.index(sorted_crms[0])
        x = x_save[index]



def check():
        global p_best, end
        last = -1 * end
        obj = p_best[last]
        for x in p_best[last:]:
            if x != obj:
                return False
        return True

def show():
        global p_best, avg_fit_crm, x

        print("x in function:",x)
        print("Best result of function:",min(p_best))
        fig, ax = plt.subplots()
        z = np.arange(max(len(p_best), len(avg_fit_crm)))
        ax.plot(z, p_best, label='Best of pop', linewidth=1)
        ax.plot(z, avg_fit_crm, label='Avg', linewidth=1)
        ax.set(xlabel='N',
               ylabel='Fitness',
               title='result')
        ax.legend()
        plt.show()



while True:
    xi = random.randrange(0, 600)
    sum = 0
    for j in range(1, 11):
        sum += (xi * xi)
    multi = cos(xi / sqrt(1)) + 1
    for j in range(2, 11):
        multi *= cos(xi / sqrt(j)) + 1
    result = (1.000 / 4000 * sum) - multi
    select = result
    for i in range(generates):
        generate()
        best_select()
        if i > 19:
            flag = check()
        if flag: break
    if flag:
        show()
        exit("End")
    else:
        print("Again!")
