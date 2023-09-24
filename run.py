from math import cos, sqrt
from random import randrange
from  matplotlib.pyplot import subplots, show
from numpy import arange # create a array ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, ...])
from sys import exit

counter = 0 # counter of generation
x = [] #
# select = []
p_best = []  # p best(result)
x_best = [] # x best
avg_fit_crm = [] # avg
xi_end = 600 # The highest value that x can have
pop = 200 # The number of crm in a generation
generates = 1000 # end of generations
end = 20 # if we found 20 same fitness in p_best we can end the programe
x_save1 = []
x_save2 = []
sum_all = 0 
gen1 = []
gen2 = []
best = 0 # best crm

def start(xi,flag):
    if flag == "Calculate":
        a = 1.0/ 4000.0
        sums = 0.0
        for j in range(1, 11):
            sums += (xi * xi)
        multi = cos(xi / sqrt(1))
        for j in range(2, 11):
            multi *= cos(xi / sqrt(j))
        result = ((a * sums) - (multi)) + 1.0
        return(result)
    
def best_select(x_save1, x_save2, gen1, gen2):
        sorted_gen1 = sorted(gen1)
        sorted_gen2 = sorted(gen2)
        if sorted_gen1[0] < sorted_gen2[0] :
            x = x_save1
        else : x = x_save2

def crossover(x_save1, x_save2, gen1, gen2):
    b = randrange(10, 200) # number of selected of best crm.
    c = 200 - b # The result shows how much space remains empty.
    gen1 = [] # free gen1
    gen1 = gen2 # replace gen1 with gen2
    x_save1 = x_save2 # replace x of gen1 with gen2
    x_save2 = x[:b]+x_save1[:c//2]+x_save2[:c//2+(c%2)] # crossover
    gen2 = [] # calculate fitness or result of new x.
    for i in range(len(x_save2)):
        gen2.append(start(x_save2[i],"Calculate"))
    print("We had {} crossover in the {} generation".format(b,counter))

def avg(x):
    z = 0
    for i in range(len(x)):
        z += x[i]
    return z/len(x)

def mutation(gen2, p_best, x, x_save2, best, counter, avg_fit_crm, x_best):
    num = randrange(-200,200) # number of mutation
    selected = [] # save selected gen
    if num > 0 :
        for i in range(num):
            random_select = randrange(0,200)
            if x_save2[random_select] != 0:
                if random_select not in selected:
                    selected.append(random_select)
                    x_save2[random_select] = best/x_save2[random_select]
                    gen2[random_select] = start(x_save2[random_select], "Calculate") # update result or fitness
    # now we must save information about p_best and avrage of fitness                   
    sorted_gen2 = sorted(gen2)
    p_best.append(sorted_gen2[0])
    x_best.append(x_save2[gen2.index(sorted_gen2[0])])
    avg_fit_crm.append(avg(gen2))
    # save best result of all
    if sorted_gen2[0] < start(best, "Calculate") : # if is better we save it.
        index  = gen2.index(sorted_gen2[0])
        best = x_save2[index]
    
    if num <= 0: num = 0 # number of mutation cant be < 0
    print("We had {} mutation in the {} generation.".format(num, counter))

def check(p_best, end):
        last = -1 * end # 20 last generation
        obj = p_best[last] # we save a fitness
        for x in p_best[last:]: # p_bet[-20:] return a array that it have 20 fitness of best
            if x != obj: # then if not equal we return false
                return False
        return True # else we return true

def shower(p_best, avg_fit_crm, best, x_best):
        print("\nx in function:", best)
        print("Best result of function:",min(p_best))
        fig, ax = subplots() # set model of plot
        ax.plot(arange((len(p_best))), p_best, label='fitness of best x', linewidth=1, marker='o')
        ax.plot(arange(len(avg_fit_crm)), avg_fit_crm, label='Avg', linewidth=1, marker='o')
        ax.plot( arange(len(x_best)), x_best, label='Best x', linewidth=1, marker='o')
        ax.set(xlabel='Generation',
               ylabel='Value',
               title='Minimum of function')
        ax.legend() 
        show()

for i in range(pop):
            a = randrange(-1*(xi_end), xi_end)
            b = randrange(-1*(xi_end), xi_end)
            c = start(a, "Calculate")
            d = start(b, "Calculate")
            gen1.append(c)
            gen2.append(d)
            x_save1.append(a)
            x_save2.append(b)

# for first generation we must save their iformation
save = sorted(gen1)
index = gen1.index(save[0])
best = x_save1[index] # save best for first time
avg_fit_crm.append(avg(gen1))
p_best.append(save[0])
x_best.append(x_save1[gen1.index(save[0])])

for i in range(2,generates): # start the generating and calculating ...
    counter += 1 # number of generation
    best_select(x_save1, x_save2, gen1, gen2)
    crossover(x_save1, x_save2, gen1, gen2)
    mutation(gen2, p_best, x, x_save2, best, counter, avg_fit_crm, x_best)
    if i > end - 1 : # because we start from 0 we must check generations to 19
        if check(p_best, end):
            shower(p_best, avg_fit_crm, best, x_best)
            exit()
shower(p_best, avg_fit_crm, best, x_best)
exit()
