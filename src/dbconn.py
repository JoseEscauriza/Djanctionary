from src.util import ROOT_DIR
import environ
import psycopg2 as pg

# Create a connection with environ
env = environ.Env()

# read .env file for connection details
environ.Env.read_env(str(ROOT_DIR / '.env'))


class Database():
    """SINGLETON CLASS for database connection"""

    _instance = None

    def __new__(cls):
        if Database._instance is None:
            Database._instance = super().__new__(cls)
            Database._instance.__init__()

        return Database._instance._conn

    def __init__(self) -> None:

        self._conn = pg.connect(
            host=env.str("db_host"),
            port=env.str("db_port"),
            user=env.str("db_user"),
            password=env.str("db_password"),
            dbname=env.str("dbname")
        )
