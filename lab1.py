import math
import random
import numpy as np
#1a
def prime(x):
    for i in range(2,x/2+1):
        if x % i == 0:
            return False
    return True
#1b
def select_primes(x):
    res = []
    for i in x:
        if prime(i):
            res.append(i)
    return res
#2a
def multiply(vec1,vec2):
    res = []
    for i in range(len(vec1)):
        res.append(vec1[i] * vec2[i])
    return res


def norm(vec):
    minimal = np.min(vec)
    maximal = np.max(vec)
    output = []
    for
    return output



print(prime(1))
        
print(select_primes([3,6,11,25,19]))


vec1 = [3,8,9,10,12]
vec2 = [8,7,7,5,6]
#2a
suma = [sum(i) for i in zip(vec1,vec2)]
print(suma)

print(multiply(vec1,vec2))

#2c
euclid = lambda vec: math.sqrt(sum([x**2 for x in vec]))
print(euclid(vec1))

#2d 0-1
rand_vec = [random.random() for i in range(50)]
print(rand_vec)

#2e
srednia = np.mean(vec1)
print("srednia",srednia)
print("min", np.min(vec1))
print("max", np.max(vec1))
odchylenie = lambda vec : math.sqrt((sum([(x - srednia)**2 for x in vec]))/len(vec))
print("odchylenie",odchylenie(vec1))

#2f
print("norm",norm(vec1))