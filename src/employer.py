class Employer:

    def __init__(self, employer_id, company_name, url):
        self.employer_id: int = employer_id
        self.company_name: str = company_name
        self.url: str = url

    def to_json_format(self) -> dict:
        """ Приводит данные к формату Json и возвращает словарь. """

        return {
            'employer_id': self.employer_id,
            'company_name': self.company_name,
            'url': self.url,
        }