import time

from src.data.db_query import DBQuery
from src.configurations.config import config


class DBCreate:

    params = config()

    @classmethod
    def create_db_and_insert_tables(cls, db_name: str, employer_ids: list) -> None:
        """ Создает базу данных и загружает в нее данные. """

        DBQuery.create_tables(db_name, cls.params)
        time.sleep(2)
        DBQuery.load_data(employer_ids, db_name)