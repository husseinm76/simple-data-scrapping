import sqlite3


def write_on_db(countries_data_list, db_file, limit=None):

    with sqlite3.connect(db_file) as connection:
        cursor = connection.cursor()

        cursor.executemany(
            """
            INSERT INTO countries(
            country_name,
            capital,
            population,
            area
            )
            VALUES (?,?,?,?)

            ON CONFLICT(country_name)
            DO UPDATE SET
                capital = excluded.capital,
                population = excluded.population,
                area = excluded.area
            """,
            countries_data_list
        )
        connection.commit()
    print(f'* {cursor.rowcount} Rows Updated')

def read_data(db_file):

    with sqlite3.Connection(db_file) as connection:
        cursor = connection.cursor()
        cursor.execute("""
            SELECT * FROM COUNTRIES
            ORDER BY id
            """,
        )

        rows = cursor.fetchall()
        return rows
    print(f'\n*** The {cursor.rowcount}  Read ***')

def db_exist(db_file_name):

    import os
    return os.path.exists(db_file_name)

def create_db(db_file):

    with sqlite3.connect(db_file) as connection:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS countries(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                country_name TEXT UNIQUE NOT NULL,
                capital TEXT,
                population INTEGER,
                area INTEGER
            )
        """)
    print('* Creat Database: Successfully')

def has_data(db_file):
    pass