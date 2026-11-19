import os

from firebird.driver import connect, driver_config

driver_config.register_server("local", """
[local]
host = localhost
""")

driver_config.register_database("minikadri", """
[minikadri]
server = local
protocol = inet
database = /db/minikadri.fdb
charset = UTF8
db_charset = UTF8
""")


def get_connection():
    return connect(
        "minikadri",
        user="SYSDBA",
        password="masterkey",
    )