from math import cos, sqrt
import random
import matplotlib.pyplot as plt
import numpy as np
from sys import exit
flag = False
crms = []
counter = 0
x = 0
g_best = []  # gbest
p_best = []  # pbest
avg_fit_crm = []
xi_end = 600
pop = 200
generates = 1000
end = 20
x_save = []
sum_all = 0 
count = 0
def start(xi):
    global xi_end, x_save, crms
    a = 1.0000 / 4000
    xi = random.randrange(0, xi_end)
    sums = 0
    for j in range(1, 11):
        sums += (xi * xi)
    multi = cos(xi / sqrt(1)) + 1
    for j in range(2, 11):
        multi *= cos(xi / sqrt(j)) + 1
    result = (a * sums) - multi
    # avg += result
    crms.append(result)
    x_save.append(xi)
    return(result)
    # avg_fit_crm.append(avg / pop)
    

# def generate():
#         global counter, pop, xi_end, crms, avg_fit_crm, select, x_save, x
#         crms = []
#         x_save = []
#         x_save.append(x)
#         crms.append(select)
#         a = 1.0000 / 4000
#         avg = 0
#         for i in range(pop - 1):
#             xi = random.randrange(0, xi_end)
#             sum = 0
#             for j in range(1, 11):
#                 sum += (xi * xi)
#             multi = cos(xi / sqrt(1)) + 1
#             for j in range(2, 11):
#                 multi *= cos(xi / sqrt(j)) + 1
#             result = (a * sum) - multi
#             avg += result
#             crms.append(result)
#             x_save.append(xi)

#         avg_fit_crm.append(avg / pop)
#         counter += 1
#         print("{} Generated.".format(counter))

def best_select():
        global crms, select, x, x_save
        x_save.append(x)
        crms.append(select)
        crms_save = crms
        sorted_crms = sorted(crms_save)
        index = crms.index(sorted_crms[0])
        x = x_save[index]


def crossover():
    global x, x_save, crms, sum_all
    a = random.randrange(-1*(len(x_save)-1),len(x_save)-1)
    if a > 0:
        print("We had a crossover in the {} generation".format(counter))
        for i in range(a):
            b = random.randrange(0,a)
            sum_all -= crms[b]
            x_save[b] = x_save[b] - x
            crms[b] = start(x_save[b])
            sum_all += crms[b]



def mutation():
    global x_save, crms, sum_all
    copy_crms = crms
    sorted_crms = sorted(copy_crms)
    if sorted_crms[0]+sorted_crms[1] > sorted_crms[0]/2.0:
        a = random.randrange(-1*(len(x_save)-1),len(x_save)-1)
        if a > 0:
            print("We had a mutation in the {} generation".format(counter))
            for i in range(a):
                b = random.randrange(0,a)
                sum_all -= crms[b]
                x_save[b]=x_save[b]/2.0
                crms[b] = start(x_save[b])
                sum_all += crms[b]

def seter():
    global crms, p_best, select, avg_fit_crm, x, sum_all, x_save, count
    crms_save = crms
    sorted_crms = sorted(crms_save)
    p_best.append(sorted_crms[0])
    select = sorted_crms[0]
    index = crms.index(sorted_crms[0])
    x = x_save[index]
    avg_fit_crm.append(sum_all/count)
    count = 0
    sum_all = 0
    crms = []
    x_save = []


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



xi = random.randrange(0, 600)
sums = 0
for j in range(1, 11):
    sums += (xi * xi)
multi = cos(xi / sqrt(1)) + 1
for j in range(2, 11):
    multi *= cos(xi / sqrt(j)) + 1
result = (1.000 / 4000 * sums) - multi
select = result
x = xi
while True:
    for i in range(generates):
        for j in range(pop - 1):
            start(random.randrange(0, 600))
            count +=1
        counter += 1
        best_select()
        crossover()
        mutation()
        seter()
        
        print("{} Generated.".format(counter))    
        if i > 18:
            flag = check()
        if flag: break
    if flag:
        show()
        exit("End")
    else:
        print("Again!")
