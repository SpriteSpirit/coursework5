import psycopg2
from src.configurations.config import config


class DBManager:

    def __init__(self, database_name: str):
        self.params = config()
        self.params.update({'dbname': database_name})
        self.conn = psycopg2.connect(**self.params)
        self.conn.autocommit = True
        self.cursor = self.conn.cursor()

    def get_companies_and_vacancies_count(self):
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

    def get_all_vacancies(self):
        """ Получает список всех вакансий у работодателей и выводит информацию о них. """

        query = """
                SELECT employers.company_name, vacancies.vacancy_name, vacancies.salary, vacancies.url
                FROM vacancies
                INNER JOIN employers ON employers.employer_id = vacancies.employer_id   
                """

        self.cursor.execute(query)
        result = self.cursor.fetchall()

        return result

    def get_avg_salary(self):
        """ Рассчитывает среднюю зарплату по вакансиям. """

        query = """
                SELECT AVG(vacancies.salary)
                FROM vacancies
                """

        self.cursor.execute(query)
        result = int(self.cursor.fetchall()[0])

        return result
