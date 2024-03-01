import psycopg2

from api.hh_api import HeadHunterAPI
from src.data.db_manager import DBManager

from src.employer import Employer
from src.vacancy import Vacancy


class DBQuery:

    @staticmethod
    def create_tables(database_name: str, params: dict) -> None:
        """ Создает базу данных и таблицы """

        # 1. проверка существования базы
        conn = psycopg2.connect(**params)
        conn.autocommit = True

        with conn.cursor() as cur:
            cur.execute('SELECT 1 FROM pg_catalog.pg_database WHERE datname = %s', database_name)
            database_exist = cur.fetchone()

            if not database_exist:
                cur.execute(f'CREATE DATABASE {database_name}')

        conn.close()

        params.update({'dbname': database_name})

        # 2. создание таблиц
        conn = psycopg2.connect()
        conn.autocommit = True

        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXIST employers (
                    employer_id serial PRIMARY KEY,
                    company_name varchar(255) NOT NULL,
                    url varchar(255)
                )
            """)

            cur.execute("""
                CREATE TABLE IF NOT EXIST vacancies (   
                    vacancy_id serial PRIMARY KEY,
                    vacancy_name varchar(255) NOT NULL,
                    employer_id int PREFERENCES employers(employer_id),
                    company_name varchar(255),
                    city varchar(255),
                    salary int,
                    url varchar(255),
                    
                    FOREIGN KEY (employer_id) REFERENCES employers(employer_id)
                )
            """)

            conn.close()

    @staticmethod
    def load_data(selected_employers: list, db_name: str) -> None:
        """
        Загружает данные о выбранных работодателях и вакансиях из API HeadHunter в базу данных.

        :param selected_employers: Список идентификаторов выбранных работодателей.
        :param db_name: Имя базы данных, в которую нужно сохранить данные.
        :return: None
        """

        hh = HeadHunterAPI()
        db_manager = DBManager(db_name)

        employers = []
        vacancies = []

        for employer in selected_employers:
            employers.append(hh.get_employer_info(employer))
            vacancies.extend(hh.get_vacancies_by_employer(employer))

        db_manager.insert_employers(Employer.cast_to_object_list(employers))
        db_manager.insert_vacancies(Vacancy.cast_to_object_list(vacancies))

        db_manager.close_connection()
