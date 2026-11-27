from math import isqrt
import random
import time

'''



>>>>>>> master
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



n = 200000033

debut = time.perf_counter()
res1 = Premier_V1(n)
t1 = time.perf_counter() - debut

debut = time.perf_counter()
res2 = Premier_V2(n)
t2 = time.perf_counter() - debut

print(f"Premier_V1({n}) = {res1} en {t1:.4f} s")
print(f"Premier_V2({n}) = {res2} en {t2:.4f} s")
print(f"Rapport t1 / t2 = {t1 / t2:.2f}")
<<<<<<< HEAD
=======

#Premier_V1(100000007) = True en 1.9327 s
#Premier_V2(100000007) = True en 0.9597 s
#Rapport t1 / t2 = 2.01

'''


def Premier_V3(n):
    """Q6 : teste 2, puis les impairs de 3 à racine(n) inclus."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for d in range(3, isqrt(n) + 1, 2):
        if n % d == 0:
            return False
    return True

def puissance_mod(a, e, n):
  """Calcule a**e mod n par carrés successifs."""
  resultat = 1
  a = a % n
  while e > 0:
    if e % 2 == 1:  # e est impair
      resultat = (resultat * a) % n
    a = (a * a) % n  # carré successif modulo n
    e = e // 2  # division entière par 2
  return resultat


def Premier_Fermat(n, k, puiss=puissance_mod):
    """Q9 : renvoie True si n est probablement premier."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    for _ in range(k):
        a = random.randint(2, n - 2)
        if puiss(a, n - 1, n) != 1:
            return False
    return True

# Test temps fermat q10)
def test_temps_fermat(n, k1=10, k2=100):
  """Mesure le temps d'exécution de Premier_Fermat pour deux valeurs de k."""
  debut = time.perf_counter()
  res1 = Premier_Fermat(n, k1)
  t1 = time.perf_counter() - debut

  debut = time.perf_counter()
  res2 = Premier_Fermat(n, k2)
  t2 = time.perf_counter() - debut

  print(f"Premier_Fermat({n}, k={k1}) = {res1} en {t1:.6f} s")
  print(f"Premier_Fermat({n}, k={k2}) = {res2} en {t2:.6f} s")
  if t1 > 0:
    print(f"Rapport t2 / t1 = {t2 / t1:.2f}")


#n = 561
#test_temps_fermat(n, k1=10, k2=1000)



# test Q11 a)
essais = 1000
faux_positifs = 0

for _ in range(essais):
  if Premier_Fermat(56052361, 10):
    faux_positifs += 1

proportion = faux_positifs / essais

print(f"Faux positifs : {faux_positifs} / {essais}")
print(f"Proportion : {proportion:.4f} (soit {proportion * 100:.2f} %)")
def decomposer(n):
    if n < 5 or n % 2 == 0:
        raise ValueError("n doit etre >= 5 et impair")

    d = n - 1
    s = 0

    while d % 2 == 0:
        d //= 2
        s += 1

    return (s, d)
