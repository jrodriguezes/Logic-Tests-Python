# 1) Profits 2.0 (Greedy + estructura)

# Tienes N ítems con cost[i] y sell[i].
# Empiezas con K dinero y tu tienda puede tener máximo 1 ítem a la vez (compras y luego vendes antes del siguiente).
# Puedes elegir cualquier orden, cada ítem a lo sumo una vez.

# Objetivo: máxima ganancia total (o dinero final).

# Input: N, K, cost[], sell[]
# Output: max_profit

def principal():
    import random as Random;
    
    items = [{
        'id': '1',
        "cost": 100,
        "sell": 150,
    }, {
        'id': '2',
        "cost": 200,
        "sell": 300,
    }, {
        'id': '3',
        "cost": 50,
        "sell": 75,
    }, {
        'id': '4',
        "cost": 120,
        "sell": 180,
    }, {
        'id': '5',
        "cost": 80,
        "sell": 120,
    }, {
        'id': '6',
        "cost": 60,
        "sell": 90,
    }]
    
    initial_random_money = Random.randint(50, 100)
    print(f"Initial random money: {initial_random_money}\n")
    
    for item in items:
        profit = 0
        if initial_random_money >= item['cost']:
            profit = item['sell'] - item['cost']
            print(f"Item ID: {item['id']}, Cost: {item['cost']}, Sell: {item['sell']}, Profit: {profit}")
            
            initial_random_money += profit
            maximum_profit = (initial_random_money + profit) - item['sell'] 
            print(f"After selling item ID {item['id']}, Profit with the initial money: {maximum_profit}, Total money gained {initial_random_money}\n")
    
    print(f"{'Final money after all transactions:':} {initial_random_money}")
    
principal()