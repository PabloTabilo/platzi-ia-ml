import random
import math
import numpy as np

def aventar_agujas(n):
    inCircle=0
    for _ in range(n):
        x,y = random.random() * random.choice([-1,1]), random.random() * random.choice([-1,1])
        dist = math.sqrt(x**2 + y**2)
        if dist <= 1:
            inCircle+=1
    return (4*inCircle)/n

def estimate(n,m):
    estimados=[]
    for _ in range(m):
        estimados.append(aventar_agujas(n))
    mean_pi = np.mean(np.array(estimados))
    std_pi = np.std(np.array(estimados))
    print(f"mu={mean_pi}, sigma={std_pi}")
    return mean_pi,std_pi

def estimarPi(precision, m):
    n=1000
    sigma=precision
    while sigma >= precision/1.96:
        media,sigma = estimate(n,m)
        n*=2

if __name__ == "__main__":
    estimarPi(0.01,1000)