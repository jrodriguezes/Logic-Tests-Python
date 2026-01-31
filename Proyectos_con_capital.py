# 2) Proyectos con capital (Greedy + heap)

# Tienes N proyectos: capital[i] (mínimo requerido) y profit[i].
# Empiezas con K capital y puedes hacer máximo M proyectos.
# Al completar uno, tu capital aumenta en profit[i]. Cada proyecto una vez.

# Objetivo: capital final máximo.


def principal():
    import random as Random

    projects = [
        {
            "id": "1",
            "capital": 100,
            "profit": 150,
        },
        {
            "id": "2",
            "capital": 200,
            "profit": 300,
        },
        {
            "id": "3",
            "capital": 50,
            "profit": 75,
        },
        {
            "id": "4",
            "capital": 120,
            "profit": 180,
        },
        {
            "id": "5",
            "capital": 80,
            "profit": 120,
        },
        {
            "id": "6",
            "capital": 60,
            "profit": 90,
        },
    ]

    initial_random_capital = Random.randint(50, 150)
    max_projects = Random.randint(2, 5)
    print(f"Maximum projects to undertake: {max_projects}")
    print(f"Initial random capital: {initial_random_capital}\n")
    projects_taken = 0
    for project in projects:

        if projects_taken == max_projects:
            print(f"Reached maximum number of projects {max_projects}.\n")
            break

        elif initial_random_capital >= project["capital"]:
            profit = project["profit"] - project["capital"]
            print(
                f"Project ID: {project['id']}, Capital Required: {project['capital']}, Profit: {profit}"
            )
            initial_random_capital += profit
            print(
                f"After completing project ID {project['id']}, Total capital gained: {initial_random_capital} Profit: {profit}\n"
            )
            projects_taken += 1
            print (f"{projects_taken}\n")

    print(f"{'Final capital after all projects:':} {initial_random_capital}")


principal()
