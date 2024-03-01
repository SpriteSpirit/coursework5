import time

from data.db_manager import DBManager
from src.data.db_query import DBQuery
from src.configurations.config import config


class DBCreate:

    params = config()

    @classmethod
    def create_db_and_insert_tables(cls, db_name: str, employer_ids: list):
        """ Создает базу данных и загружает в нее данные. """

        DBQuery.create_tables(db_name, cls.params)
        time.sleep(2)
        db_manager = DBQuery.load_data(db_name, employer_ids)

        return db_manager
