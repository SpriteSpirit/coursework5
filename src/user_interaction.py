

def print_all_companies_and_vacancies(total_list: list) -> None:
    for items in total_list:
        print(items)

    all_vacancies = sum([vac[1] for vac in total_list])

    print(f"\nКомпаний: {len(total_list)}\nВакансий: {all_vacancies}")