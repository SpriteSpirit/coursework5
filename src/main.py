from src.data.db_create import DBCreate
from src.storage.json_saver import JSONSaver
from user_interaction import *

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


def main_menu():
    """ Главное меню для выбора действий """

    db_name = 'db_hh'
    db_manager = DBCreate.create_db_and_insert_tables(db_name, selected_employers)

    print("(👉ﾟヮﾟ)👉 Добро пожаловать в JobFinder v2.0!\n")

    while True:
        print('Выберите пункт меню:')
        print('[1 : количество вакансий по выбранным компаниям]')
        print('[2 : все вакансии по выбранным компаниям]')
        print('[3 : среднюю заработную плату по всем вакансиям]')
        print('[4 : вакансии с зарплатой выше средней]')
        print('[5 : вакансии с ключевым словом]')
        print('[0 : выйти]')

        user_choice = input('::=> ')

        try:
            user_choice = int(user_choice)

            if user_choice == 1:
                # ---------- companies_and_vacancies ----------#
                companies_and_vacancies = db_manager.get_companies_and_vacancies_count()
                print_all_companies_and_vacancies(companies_and_vacancies)
                JSONSaver.save_into_json_file(companies_and_vacancies, 'companies_and_vacancies')
            elif user_choice == 2:
                # ---------- all_vacancies ----------#
                all_vacancies = db_manager.get_all_vacancies()
                print_all_vacancies(all_vacancies)
                JSONSaver.save_into_json_file(all_vacancies, 'all_vacancies')
            elif user_choice == 3:
                # ---------- avg_salary ----------#
                avg_salary = db_manager.get_avg_salary()
                print_avg_salary(avg_salary)
            elif user_choice == 4:
                # ---------- vacancies_higher_avg_salary ----------#
                vacancies_higher_avg_salary = db_manager.get_vacancies_with_higher_salary()
                print_vacancies_higher_avg_salary(vacancies_higher_avg_salary)
                JSONSaver.save_into_json_file(vacancies_higher_avg_salary, 'vacancies_higher_avg_salary')
            elif user_choice == 5:
                # ---------- vacancies_with_keyword ----------#
                user_keyword = input('Введите ключевое слово для поиска\n::=> ')
                vacancies_with_keyword = db_manager.get_vacancies_with_keyword(user_keyword)
                print_vacancies_with_keyword(vacancies_with_keyword)
                JSONSaver.save_into_json_file(vacancies_with_keyword, 'vacancies_with_keyword')
            elif user_choice == 0:
                print("Спасибо за то, что воспользовались JobFinder v2.0! 👈(ﾟヮﾟ👈)")
                quit()
        except ValueError:
            print('Неверный ввод. Попробуйте снова.')


if __name__ == '__main__':
    main_menu()
