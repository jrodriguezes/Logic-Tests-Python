def main():
    import random as random
# Dado S (solo dígitos), cuenta cuántas formas de partirlo en partes tal que:

# cada número ≤ C

# sin ceros a la izquierda (excepto “0” como número único sí se permite)

# usar todo el string

# respuesta módulo 10^K

# Input: N C K y S
# Output: count % (10**K)
    number_list = []
    i = 0
    
    while i < 5:
        random_number = random.randint(1, 999999999)
        number_list.append(random_number)
        i += 1
        
    cannot_be_lower_than_this_number = random.randint(1, 300)
    
    for number in number_list:
        parted_number = 