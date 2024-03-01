from src.data.db_create import DBCreate
from src.storage.json_saver import JSONSaver
from user_interaction import *


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
    companies_and_vacancies = db_manager.get_companies_and_vacancies_count()
    print_all_companies_and_vacancies(companies_and_vacancies)
    JSONSaver.save_into_json_file(companies_and_vacancies, 'companies_and_vacancies')

    # ---------- all_vacancies ----------#
    all_vacancies = db_manager.get_all_vacancies()
    print_all_vacancies(all_vacancies)
    JSONSaver.save_into_json_file(all_vacancies, 'all_vacancies')

    # ---------- avg_salary ----------#
    avg_salary = db_manager.get_avg_salary()
    print_avg_salary(avg_salary)

    # ---------- vacancies_higher_avg_salary ----------#
    vacancies_higher_avg_salary = db_manager.get_vacancies_with_higher_salary()
    print_vacancies_higher_avg_salary(vacancies_higher_avg_salary)
    JSONSaver.save_into_json_file(vacancies_higher_avg_salary, 'vacancies_higher_avg_salary')


if __name__ == '__main__':
    main()
