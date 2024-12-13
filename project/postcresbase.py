"""
This is a file working only with the PostgreSQL db
"""

import psycopg2
from psycopg2 import sql

from dotenv_ import (APP_POSTGRES_HOST, APP_POSTGRES_LOGIN, APP_POSTGRES_PASS,
                     APP_POSTGRES_PORT)


def create_database_if_not_exsists(db_name: str) -> bool:
    """
    Def is only checking db. From entry point ('db_name') we receive a db name\
    and her will be look up in inside the postgresql. When returns the 'True' \
    it means what we not have a db name or 'False'.
    :param db_name: str This is a db name.
    :return:bool.
    """
    connection = psycopg2.connect(
        user=f"{APP_POSTGRES_LOGIN}",
        password=f"{APP_POSTGRES_PASS}",
        host=f"{APP_POSTGRES_HOST}",
        port=f"{APP_POSTGRES_PORT}",
    )
    # AUTOCOMMIT
    connection.autocommit = True

    # CURSOR
    cursor = connection.cursor()

    # CHECK availability the tb_name of the postgres
    cursor.execute(sql.SQL("SELECT 1 FROM pg_database WHERE datname = %s"), [db_name])
    exists = cursor.fetchone()

    status_text = "None"
    status = False
    if not exists:
        sql_text = f"CREATE DATABASE {db_name}"
        cursor.execute(sql.SQL(sql_text))
        status_text = status_text.replace(
            "None", f"[postgreSQL]: База данных '{db_name}' успешно создана."
        )
        status = True
    else:
        status_text = status_text.replace(
            "None", f"[postgreSQL]: База данных '{db_name}' уже существует."
        )

    print(status_text)
    # CLOSE the connection
    cursor.close()
    connection.close()

    return status
