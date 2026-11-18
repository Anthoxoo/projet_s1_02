def Premier_V1(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True





def Premier_V2(n):
    if n < 2:
        return False
    if n == 2:
        return True    
    if n % 2 == 0:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print(Premier_V2(1))
print(Premier_V1(1))