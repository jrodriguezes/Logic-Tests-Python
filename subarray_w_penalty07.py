#     Dado un array A y un valor P, define la “ganancia” de un subarray como:
#     sum(subarray) - P * (len(subarray)-1)

#     Objetivo: máximo valor posible.


def maximum_gain_w_penalty(Array, P):
    current_index = Array[0]
    current_gain = 0

    best_gain = Array[0]
    best_start = 0
    best_end = 0
    
    for i in range(1, len(Array)):
        gain_if_start_new = Array[i]
        gain_if_extend = current_gain + Array[i] - P

        # choose which subarray ends at i
        if gain_if_start_new >= gain_if_extend:
                    current_gain = gain_if_start_new
                    current_start = i
        else:
            current_gain = gain_if_extend

        # update global best
        if current_gain > best_gain:
                    best_gain = current_gain
                    best_start = current_start
                    best_end = i

    return best_gain, best_start, best_end

def principal():
    import random as random
    randomP = random.randint(1, 4)

    i = 0
    Array = []
    
    while i < 15:
        randomValue = random.randint(-30, 80)
        Array.append(randomValue)
        i += 1
    
    best_gain, best_start, best_end = maximum_gain_w_penalty(Array, randomP)
    
    print(f"Best gain: {best_gain}, Best start: {best_start}, Best end: {best_end}, Subarray {Array[best_start:best_end]}")
    
    
principal()