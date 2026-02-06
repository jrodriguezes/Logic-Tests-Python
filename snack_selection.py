def principal():
    
# Tienes N snacks con:

# sat[i] satisfacción

# cal[i] calorías

# cost[i] costo

# Puedes comprar cada snack a lo sumo una vez.
# Necesitas satisfacción total ≥ X y calorías totales ≤ Y.

# Objetivo: costo mínimo (se garantiza que existe solución).

    import random as Random

    snacks = [{
        "id": "1",
        "sat": 98,
        "cal": 250,
        "cost": 4,
    }, {
        "id": "2",
        "sat": 90,
        "cal": 300,
        "cost": 5,
    }, {
        "id": "3",
        "sat": 80,
        "cal": 200,
        "cost": 3,
    }, {
        "id": "4",
        "sat": 70,
        "cal": 400,
        "cost": 7,
    }, {
        "id": "5",
        "sat": 100,
        "cal": 150,
        "cost": 2,
    }, {
        "id": "6",
        "sat": 50,
        "cal": 500,
        "cost": 8,
    }, {
        "id": "7",
        "sat": 60,
        "cal": 350,
        "cost": 6,
    }, {
        "id": "8",
        "sat": 85,
        "cal": 275,
        "cost": 4,
    }, {
        "id": "9",
        "sat": 95,
        "cal": 225,
        "cost": 3,
    }, {
        "id": "10",
        "sat": 75,
        "cal": 450,
        "cost": 7,
    }, {
        "id": "11",
        "sat": 65,
        "cal": 375,
        "cost": 5,
    }]
    
    
    total_satisfaction = Random.randint(200, 400)
    total_calories = Random.randint(500, 1200)
    
    print(f"Desired total satisfaction: {total_satisfaction}")
    print(f"Calorie limit: {total_calories}\n")
    
    sorted_by_lower_cost = sorted(snacks, key=lambda x: x["cost"])
    acumulated_sat = 0
    acumulated_cal = 0
    
    for x in sorted_by_lower_cost:

        if (acumulated_sat >= total_satisfaction) and (acumulated_cal <= total_calories):
            print(f"Reached desired satisfaction {total_satisfaction} and calorie limit {total_calories}.\n")
            break
        else:
            acumulated_sat += x["sat"]
            acumulated_cal += x["cal"]
            print(acumulated_sat)
            print(acumulated_cal)

            print(
                f"Snack ID: {x['id']}, Satisfaction: {x['sat']}, Calories: {x['cal']}, Cost: {x['cost']}"
            )
            print(
                f"After choosing snack ID {x['id']}, Total Satisfaction: {acumulated_sat}, Total Calories: {acumulated_cal}\n"
            )
            
principal()