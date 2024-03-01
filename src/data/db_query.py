import psycopg2


def create_tables(database_name: str, params: dict) -> None:
    """ Создает базу данных и таблицы """

    # 1. проверка существования базы
    conn = psycopg2.connect(**params)
    conn.autocommit = True

    with conn.cursor() as cur:
        cur.execute('SELECT 1 FROM pg_catalog.pg_database WHERE datname = %s', database_name)
        database_exist = cur.fetchone()

        if not database_exist:
            cur.execute(f'CREATE DATABASE {database_name}')

    conn.close()

    params.update({'dbname': database_name})

    # 2. создание таблиц
    conn = psycopg2.connect()
    conn.autocommit = True

    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXIST employers (
                employer_id serial PRIMARY KEY,
                company_name varchar(255) NOT NULL,
                url varchar(255)
            )
        """)

        cur.execute("""
            CREATE TABLE IF NOT EXIST vacancies (   
                vacancy_id serial PRIMARY KEY,
                vacancy_name varchar(255) NOT NULL,
                employer_id int PREFERENCES employers(employer_id),
                company_name varchar(255),
                city varchar(255),
                salary int,
                url varchar(255),
                
                FOREIGN KEY (employer_id) REFERENCES employers(employer_id)
            )
        """)

        conn.close()
