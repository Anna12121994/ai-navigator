from graph import locations
from dijkstra import dijkstra
from database import create_table, save_route


create_table()

print("NAVIGATOR")
print()

for key, value in locations.items():
    print(key, "-", value)

print()

start = input("Початкова точка: ").upper()
finish = input("Кінцева точка: ").upper()

if start not in locations or finish not in locations:
    print("Такої точки не існує")

else:
    route, distance, time = dijkstra(start, finish)

    print()
    print("Знайдений маршрут:")
    print(" → ".join(route))

    print("Відстань:", distance, "км")
    print("Час:", time, "хв.")

    save_route(
        start,
        finish,
        route,
        distance,
        time
    )