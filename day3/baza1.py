# bazy danych - relacyjne, nieralacyjne
# silnik - mechanizm przechowywania, przetwarzania danych
# sql, nosql
# mssql, oracle, mysql, mariadb, postgress, teradata, sqlite

import sqlite3

try:
    conn = sqlite3.connect("baza_danych.db")

    c = conn.cursor()
    print("Baza danych została podłączona")
except sqlite3.Error as e:
    print("Błąd:", e)
finally:
    if conn:
        conn.close()
        print("Połączenie zostało zamknięte")
