import time


def Premier_V1_compte(n):
  if n < 2:
    return False, 0
  operations = 0
  for i in range(2, n):  #[cite: 2]
    operations += 1
    if n % i == 0:  #[cite: 2]
      return False, operations
  return True, operations


# Choix d'un nombre premier assez grand pour durer quelques secondes (ex. 10**7 + 19)
# Tu peux tester aussi n = 10**8 + 7 (plus long)
n = 10**7 + 19

debut = time.perf_counter()
est_premier, nb_ops = Premier_V1_compte(n)
duree = time.perf_counter() - debut

ops_par_seconde = nb_ops / duree

print(f"Résultat : {est_premier}")
print(f"Nombre d'itérations effectuées : {nb_ops}")
print(f"Temps écoulé : {duree:.4f} s")
print(f"Vitesse mesurée : {ops_par_seconde:,.0f} itérations / seconde")