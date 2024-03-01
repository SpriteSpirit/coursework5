import requests


class HeadHunterAPI:
    """ Класс получает информацию по вакансиям и работодателям """
    vacancies_url = 'https://api.hh.ru/vacancies'
    employers_url = 'https://api.hh.ru/employers'

    def __init__(self, keyword: str = None):
        self.params = {
            'area': '113',
            'text': keyword,
            'search_field': 'company_name',
            'per_page': 100,
            'page': 0,
            'only_with_vacancies': True,
            'only_with_salary': True,
        }

    def get_all_vacancies_info(self, pages: int = 2) -> list:
        """
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
