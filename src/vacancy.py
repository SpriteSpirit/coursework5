class Vacancy:

    def __init__(self, vacancy_id, vacancy_name, employer_id, company_name, city, salary, url):
        self.vacancy_id: int = vacancy_id
        self.vacancy_name: str = vacancy_name
        self.employer_id: int = employer_id
        self.company_name: str = company_name
        self.city: str = city
        self.salary: float = salary
        self.url: str = url

    def to_json_format(self) -> dict:
        """ Приводит данные к формату Json и возвращает словарь. """

        return {
            'vacancy_id': self.vacancy_id,
            'vacancy_name': self.vacancy_name,
            'employer_id': self.employer_id,
            'company_name': self.company_name,
            'city': self.city,
            'salary': self.salary,
            'url': self.url,
        }
