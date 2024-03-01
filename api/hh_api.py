import requests


class HeadHunterAPI:
    """ Класс получает информацию по вакансиям и работодателям """
    vacancies_url = 'https://api.hh.ru/vacancies'
    employers_url = 'https://api.hh.ru/employers'

    def __init__(self, keyword: str = None):
        self.params = {
            'area': '113',
            'text': keyword,
            'per_page': 100,
            'page': 0,
            'only_with_vacancies': True,
            'only_with_salary': True,
        }

    def get_all_vacancies_info(self, pages: int = 1) -> list:
        """
        Возвращает список вакансий по ключевому запросу или все по-заданному кол-ву страниц.
        :pages: int: - index - количество страниц для поиска
        :return: Список всех найденных вакансий
        """
        all_vacancies = []

        response = requests.get(url=self.vacancies_url, params=self.params)
        data = response.json()

        # Добавляем вакансии с первой страницы
        all_vacancies.extend(data['items'])

        # Пока есть следующая страница, добавляем вакансии в список
        while data['pages'] > data['page'] != pages - 1:
            self.params['page'] = data['page'] + 1
            response = requests.get(url=self.vacancies_url, params=self.params)
            data = response.json()
            all_vacancies.extend(data['items'])

        return all_vacancies

    def get_employer_info(self, employer_ids: list) -> list:
        """
        Получает информацию о каждом работодателе.
        :param employer_ids: Список идентификаторов работодателей для получения информации.
        :return: Список словарей с информацией о работодателях.
        """
        favourite_employers = []

        for employer_id in employer_ids:
            response = requests.get(f'{self.employers_url}/{employer_id}', self.params)
            data = response.json()
            favourite_employers.append(data)

        return favourite_employers

    def get_vacancies_by_employer(self, employer_id: int) -> list:
        """
        Получает информацию о вакансиях для указанного работодателя.
        :param employer_id: Идентификатор работодателя, для которого нужно получить информацию о вакансиях.
        :return: Список словарей с информацией о вакансиях для указанного работодателя.
        """
        response = requests.get(f'{self.vacancies_url}?employer_id={employer_id}', self.params)
        data = response.json()['items']

        return data
