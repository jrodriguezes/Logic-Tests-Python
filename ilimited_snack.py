def principal():
    # Lo mismo que el anterior, pero ahora cada snack se puede comprar infinitas veces.

    # Objetivo: costo mínimo.
    import random as Random

    snacks = [
        {
            "id": "1",
            "sat": 98,
            "cal": 250,
            "cost": 4,
        },
        {
            "id": "2",
            "sat": 90,
            "cal": 300,
            "cost": 5,
        },
        {
            "id": "3",
            "sat": 80,
            "cal": 200,
            "cost": 3,
        },
        {
            "id": "4",
            "sat": 70,
            "cal": 400,
            "cost": 7,
        },
        {
            "id": "5",
            "sat": 100,
            "cal": 150,
            "cost": 2,
        },
        {
            "id": "6",
            "sat": 50,
            "cal": 500,
            "cost": 8,
        },
        {
            "id": "7",
            "sat": 60,
            "cal": 350,
            "cost": 6,
        },
        {
            "id": "8",
            "sat": 85,
            "cal": 275,
            "cost": 4,
        },
        {
            "id": "9",
            "sat": 95,
            "cal": 225,
            "cost": 3,
        },
        {
            "id": "10",
            "sat": 75,
            "cal": 450,
            "cost": 7,
        },
        {
            "id": "11",
            "sat": 65,
            "cal": 375,
            "cost": 5,
        },
        {
            "id": "12",
            "sat": 110,
            "cal": 100,
            "cost": 1,
        },
        {
            "id": "13",
            "sat": 45,
            "cal": 600,
            "cost": 9,
        },
        {
            "id": "14",
            "sat": 120,
            "cal": 80,
            "cost": 2,
        },
        {
            "id": "15",
            "sat": 55,
            "cal": 550,
            "cost": 7,
        },
        {
            "id": "16",
            "sat": 130,
            "cal": 70,
            "cost": 3,
        },
        {
            "id": "17",
            "sat": 40,
            "cal": 650,
            "cost": 10,
        },
        {
            "id": "18",
            "sat": 140,
            "cal": 60,
            "cost": 4,
        },
        {
            "id": "19",
            "sat": 35,
            "cal": 700,
            "cost": 11,
        },
        {
            "id": "20",
            "sat": 150,
            "cal": 50,
            "cost": 5,
        },
        {
            "id": "21",
            "sat": 30,
            "cal": 750,
            "cost": 12,
        },
        {
            "id": "22",
            "sat": 160,
            "cal": 40,
            "cost": 6,
        },
        {
            "id": "23",
            "sat": 25,
            "cal": 800,
            "cost": 13,
        },
        {
            "id": "24",
            "sat": 170,
            "cal": 30,
            "cost": 7,
        },
        {
            "id": "25",
            "sat": 20,
            "cal": 850,
            "cost": 14,
        },
    ]

    total_satisfaction = Random.randint(2000, 4000)
    total_calories = Random.randint(5000, 12000)

    print(f"Desired total satisfaction: {total_satisfaction}")
    print(f"Calorie limit: {total_calories}\n")

    sorted_by_lower_cost = sorted(snacks, key=lambda x: x["cost"])

    acumulated_sat = 0
    acumulated_cal = 0

    while acumulated_sat < total_satisfaction:
            
        for x in sorted_by_lower_cost:
            
            if (acumulated_sat >= total_satisfaction):
                break
            
            if (acumulated_cal + x['cal'] > total_calories):
                continue
            
            acumulated_sat += x["sat"]
            acumulated_cal += x["cal"]
            
            print(acumulated_sat)
            print(acumulated_cal)

            print(f"Buy snack {x['id']} +sat {x['sat']} +cal {x['cal']} Totals -> sat= {acumulated_sat}, cal= {acumulated_cal}"
            )
            
    if acumulated_sat >= total_satisfaction and acumulated_cal <= total_calories:
        print("\nVALIDACIÓN CUMPLIDA")
        print(f"Satisfaction: {acumulated_sat} ≥ {total_satisfaction}")
        print(f"Calories: {acumulated_cal} ≤ {total_calories}")
    else:
        print("\nVALIDACIÓN NO CUMPLIDA")

principal()
