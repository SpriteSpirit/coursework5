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

    def get_employer_info(self, employer_id: list) -> list:
        """
        Получает информацию о каждом работодателе.
        :param employer_id: Идентификатор работодателя для получения информации.
        :return: Список словарей с информацией о работодателях.
        """

        response = requests.get(f'{self.employers_url}/{employer_id}', self.params)
        data = response.json()

        return data

    def get_vacancies_by_employer(self, employer_id: int) -> list:
        """
        Получает информацию о вакансиях для указанного работодателя.
        :param employer_id: Идентификатор работодателя, для которого нужно получить информацию о вакансиях.
        :return: Список словарей с информацией о вакансиях для указанного работодателя.
        """
        response = requests.get(f'{self.vacancies_url}?employer_id={employer_id}', self.params)
        data = response.json()['items']

        return data
