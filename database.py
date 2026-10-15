import psycopg2


def connect_db():
    connection = psycopg2.connect(
        host="localhost",
        database="navigator",
        user="postgres",
        password="Nesk.121294",
        port="5433"
    )

    return connection


def create_table():
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS routes (
            id SERIAL PRIMARY KEY,
            start_point VARCHAR(10),
            finish_point VARCHAR(10),
            route TEXT,
            distance FLOAT,
            time FLOAT,
            traffic FLOAT,
            actual_time FLOAT,
            actual_distance FLOAT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    connection.commit()
    cursor.close()
    connection.close()


def save_route(start_point, finish_point, route, distance, time):
    connection = connect_db()
    cursor = connection.cursor()

    route_text = ",".join(route)

    cursor.execute("""
        INSERT INTO routes (
            start_point,
            finish_point,
            route,
            distance,
            time
        )
        VALUES (%s, %s, %s, %s, %s)
    """, (
        start_point,
        finish_point,
        route_text,
        distance,
        time
    ))

    connection.commit()

    cursor.close()
    connection.close()

    print("Маршрут збережено в базу даних.")