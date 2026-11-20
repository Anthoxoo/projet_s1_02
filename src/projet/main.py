
def Premier_V1(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

#le même, mais on rajoute 2 opérations supplémentaire O (n)
def Premier_V2(n):
    if n < 2:
        return False
    if n == 2:
        return True    
    if n % 2 == 0:
        return False
    for i in range(3, n, 2):
        if n % i == 0:
            return False
    return True

import time

n = (10**8 + 7)*2

debut = time.perf_counter()
res1 = Premier_V1(n)
t1 = time.perf_counter() - debut

debut = time.perf_counter()
res2 = Premier_V2(n)
t2 = time.perf_counter() - debut

print(f"Premier_V1({n}) = {res1} en {t1:.4f} s")
print(f"Premier_V2({n}) = {res2} en {t2:.4f} s")
print(f"Rapport t1 / t2 = {t1 / t2:.2f}")

#Premier_V1(100000007) = True en 1.9327 s
#Premier_V2(100000007) = True en 0.9597 s
#Rapport t1 / t2 = 2.01