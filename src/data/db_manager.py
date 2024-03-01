import psycopg2
from src.configurations.config import config


class DBManager:

    def __init__(self, database_name: str):
        self.params = config()
        self.params.update({'dbname': database_name})
        self.conn = psycopg2.connect(**self.params)
        self.conn.autocommit = True
        self.cursor = self.conn.cursor()

    def get_companies_and_vacancies_count(self) -> int:
        """ Получает список всех компаний и количество вакансий у каждой компании. """

        query = """
            SELECT employers.company_name, COUNT(vacancies.vacancy_id) AS vacancies_count
            FROM employers
            LEFT JOIN vacancies ON employers.employer_id = vacancies.employer_id   
            GROUP BY employers.company_name     
        """

        self.cursor.execute(query)
        result = self.cursor.fetchall()

        return result