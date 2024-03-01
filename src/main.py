from src.data.db_create import DBCreate
from src.storage.json_saver import JSONSaver
from user_interaction import print_all_companies_and_vacancies


def main():
    """  """

    selected_employers = [
        1795976,
        5686111,
        14809,
        865831,
        4295296,
        1227460,
        65660,
        2097195,
        1144757,
        2365329,
    ]

    db_name = 'db_hh'
    db_manager = DBCreate.create_db_and_insert_tables(db_name, selected_employers)

    # ---------- companies_and_vacancies ----------#
    print("Компании и количество вакансий:")
    companies_and_vacancies = db_manager.get_companies_and_vacancies_count()
    print_all_companies_and_vacancies(companies_and_vacancies)

    # ---------- all_vacancies ----------#
    print(f"\nВсе вакансии:")
    all_vacancies = db_manager.get_all_vacancies()


if __name__ == '__main__':
    main()
