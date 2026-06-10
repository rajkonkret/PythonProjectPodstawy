# bazy danych - relacyjne, nieralacyjne
# silnik - mechanizm przechowywania, przetwarzania danych
# sql, nosql
# mssql, oracle, mysql, mariadb, postgress, teradata, sqlite
# https://sqlitebrowser.org/

import sqlite3

try:
    conn = sqlite3.connect("baza_danych.db")

    c = conn.cursor()
    print("Baza danych została podłączona")

    query = """
    CREATE TABLE IF NOT EXISTS developers (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    salary REAL NOT NULL);
    """

    c.execute(query)
    conn.commit()

    insert = "INSERT INTO developers (id,name,salary) VALUES (2, 'Radek', 1500);"
    # c.execute(insert)
    # conn.commit()

    select = "SELECT * FROM developers;"
    for row in c.execute(select):
        print(row)
        # (1, 'Radek', 1500.0)
        # (2, 'Radek', 1500.0)

except sqlite3.Error as e:
    print("Błąd:", e)
finally:
    if conn:
        conn.close()
        print("Połączenie zostało zamknięte")
