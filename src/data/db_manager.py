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
        """ Возвращает список всех компаний и количество вакансий у каждой компании. """

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
        """ Возвращает все вакансии у работодателей и выводит информацию о них. """

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

    def get_vacancies_with_higher_salary(self):
        """ Возвращает список вакансий, у которых зарплата выше средней по всем вакансиям. """

        avg_salary = self.get_avg_salary()

        query = """
                SELECT *
                FROM vacancies
                WHERE vacancies.salary > %s
                """

        self.cursor.execute(query, avg_salary)
        result = self.cursor.fetchall()

        return result

    def get_vacancies_with_keyword(self, keyword: str):
        """ Возвращает список всех вакансий, содержащих ключевое слово. """

        query = """
               SELECT * 
               FROM vacancies
               WHERE LOWER(vacancies.vacancy_name) LIKE LOWER(%s)
               """

        self.cursor.execute(query, f'%{keyword}%')
        result = self.cursor.fetchall()

        return result

    def insert_vacancies(self, vacancies: list):
        """ Добавляет вакансию из списка вакансий в БД. """

        query = """
               INSERT INTO vacancies (vacancy_id, vacancy_name, employer_id, company_name, city, salary, url) 
               VALUES (%s, %s, %s, %s, %s, %s, %s)
               """

        for vacancy in vacancies:
            self.cursor.execute(
                query, (vacancy.vacancy_id, vacancy.vacancy_name, vacancy.employer_id, vacancy.company_name,
                        vacancy.city, vacancy.salary, vacancy.url)
            )

    def insert_employers(self, employers: list):
        """ Добавляет работодателей из списка в БД """

        query = """
               INSERT INTO employers (employer_id, company_name, url) 
               VALUES (%s, %s, %s)
               """

        for employer in employers:
            self.cursor.execute(
                query, (employer.employer_id, employer.company_name, employer.url)
            )

    def close_connection(self):
        """ Закрывает соединение с базой данных. """

        return self.conn.close()
