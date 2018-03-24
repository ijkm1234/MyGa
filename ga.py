
import math
import random
import matplotlib.pyplot as plt
import numpy as np

def iniPop(pop_size,chrom_length):
    pop=[]
    for i in range(pop_size):
        chrom=[]
        for j in range(chrom_length):
            chrom.append(random.randint(0,1))
        pop.append(chrom)
    return pop

def decode(pop):
    val=[]
    for i in pop:
        x=0
        bit=len(i)-1
        for j in i:
            x+=j*(2**bit)
            bit=bit-1
        val.append(x)
    return val

def cal_adpval(decodePop):
    adpval=[]
    for x in decodePop:
        y = x**3-60*x**2+900*x+100
        adpval.append(y)
    return adpval

def choose_parent(pop):
    adpval=cal_adpval(decode(pop))
    p=[]
    for i in adpval:
        p.append(i/sum(adpval))
    P=[]
    x=0
    for i in p:
        x+=i
        P.append(x)
    parent=[]
    for i in range(len(pop)):
        e=random.random()
        for j in P:
            if e<j:
                parent.append(pop[P.index(j)])
                break
    return parent

def cross(pop,cp):
    random.shuffle(pop)
    for i in range(0,len(pop),2):
        if (random.random()<cp):
            cpoint=random.randint(1,len(pop[0])-1)
            temp1=[]
            temp2=[]
            temp1.extend(pop[i][0:cpoint])
            temp1.extend(pop[i+1][cpoint:])
            temp2.extend(pop[i+1][0:cpoint])
            temp2.extend(pop[i][cpoint:])
            pop[i]=temp1
            pop[i+1]=temp2

def mutation(pop,mp):
    for i in pop:
        if (random.random()<mp):
            mpoint=random.randint(0,len(i)-1)
            if (i[mpoint]==1):
                i[mpoint]=0
            else:
                i[mpoint]=1

if __name__=='__main__':
    pop_num=60
    chrom_len=5
    pop=iniPop(pop_num,chrom_len)
    NG=600
    result=[]
    arv=[]
    for i in range(NG):
        pop=choose_parent(pop)
        cross(pop,0.9)
        mutation(pop,0.02)
        print(decode(pop))
        print(max(cal_adpval(decode(pop))))
        result.append(max(cal_adpval(decode(pop))))
        arv.append(np.mean(cal_adpval(decode(pop))))
    plt.plot(range(NG),result)
    plt.plot(range(NG),arv)
    plt.show()


