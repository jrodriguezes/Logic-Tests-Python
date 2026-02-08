def count_partitions(S, C, K):
    MOD = 10 ** K
    n = len(S)
    
    dp = [0] * (n + 1) # List of 0, [0,0,0,0]
    dp[0] = 1  # Base case: there's one way to partition an empty string
    
    print('dp inicial ',dp)
    print('S ',S)
    print('n',n)
    print('C',C)
    for i in range(n):
        print('i justo despues del bucle ',i)
        print('dp[i] ',dp[i])
        print(dp)

        if dp[i] == 0:
            continue
        
        # Si empieza con 0, solo podés tomar "0" como número único
        if S[i] == '0':
            # tomar solo "0"
            if 0 <= C:
                dp[i + 1] = (dp[i + 1] + dp[i]) % MOD
            continue

        # construir números desde i hacia adelante
        val = 0
        for j in range(i, n):
            val = val * 10 + (ord(S[j]) - ord('0'))
            if val > C:
                break
            dp[j + 1] = (dp[j + 1] + dp[i]) % MOD

    return dp[n] % MOD
    

def main():
    import random as random
# Dado S (solo dígitos), cuenta cuántas formas de partirlo en partes tal que:

# cada número ≤ C

# sin ceros a la izquierda (excepto “0” como número único sí se permite)

# usar todo el string

# respuesta módulo 10^K

# Input: N C K y S
# Output: count % (10**K)
    List_S = []
    List_C = []
    i = 0
    K = 3
    while i <= 5:
        S = str(random.randint(0, 10**9))
        List_S.append(S)
        C = random.randint(1, 10**3)
        List_C.append(C)
        i += 1
        
    for idx in range(len(List_S)):
        S = List_S[idx]
        C = List_C[idx]
        ans = count_partitions(S, C, K)
        print(f"Caso {idx+1}: S={S}, C={C}, K={K} -> respuesta={ans}")

main()