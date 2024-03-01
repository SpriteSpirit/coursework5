

def print_all_companies_and_vacancies(total_list: list) -> None:
    """ Выводит в консоль все компании и кол-во вакансий """

    print("Компании и количество вакансий:")

    for company, vacancies_count in total_list:
        print(f'{company} : {vacancies_count} ')

    all_vacancies = sum([vac[1] for vac in total_list])

    print(f"\nКомпаний: {len(total_list)}\nВакансий: {all_vacancies}")


def print_all_vacancies(total_list: list) -> None:
    """ Выводит в консоль все вакансии выбранных компаний """

    print_dict = {}

    for vacancy in total_list:
        company_name = vacancy[0]
        vacancy_details = f'{vacancy[1]}, {vacancy[2]} RUB, {vacancy[3]}'

        if company_name in print_dict:
            print_dict[company_name].append(vacancy_details)
        else:
            print_dict[company_name] = [vacancy_details]

    print(f"\nВсе вакансии:")

    # Выводим вакансии для каждой компании
    for company, vacancies in print_dict.items():
        print(f'\n{company}:')
        for i, vacancy_details in enumerate(vacancies, 1):
            print(f'{i}. {vacancy_details}')


def print_avg_salary(avg_salary: float) -> None:
    """ Выводит среднюю зарплату по вакансиям """
    print(f"Средняя зарплата по вакансиям: {avg_salary} RUB.")


def print_vacancies_higher_avg_salary(total_list: list) -> None:
    """ Выводит вакансии с зарплатой выше средней """

    print_dict = {}

    for vacancy in total_list:
        company_name = vacancy[3]
        vacancy_details = {'Вакансия': vacancy[1], 'Город': vacancy[4], 'Зарплата': f'{vacancy[5]} RUB',
                           'Ссылка': vacancy[6], 'ID вакансии': vacancy[0], 'ID компании': vacancy[2]}

        if company_name in print_dict:
            print_dict[company_name].append(vacancy_details)
        else:
            print_dict[company_name] = [vacancy_details]

    print(f"\nВакансии с зарплатой выше средней:")

    # Выводим вакансии для каждой компании
    for company, vacancies in print_dict.items():
        print(f'\n{company}:')
        for i, vacancy_details in enumerate(vacancies, 1):
            print(f'{i}. {vacancy_details}')


def print_vacancies_with_keyword(total_list: list) -> None:
    """ Выводит все вакансии, содержащие ключевое слово в запросе """

    print_dict = {}

    for vacancy in total_list:
        company_name = vacancy[3]
        vacancy_details = {'Вакансия': vacancy[1], 'Город': vacancy[4], 'Зарплата': f'{vacancy[5]} RUB',
                           'Ссылка': vacancy[6], 'ID вакансии': vacancy[0], 'ID компании': vacancy[2]}

        if company_name in print_dict:
            print_dict[company_name].append(vacancy_details)
        else:
            print_dict[company_name] = [vacancy_details]

    print(f"\nВакансии, содержащие ключевое слово:")

    # Выводим вакансии для каждой компании
    for company, vacancies in print_dict.items():
        print(f'\n{company}:')
        for i, vacancy_details in enumerate(vacancies, 1):
            print(f'{i}. {vacancy_details}')
