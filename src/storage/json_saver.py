import json
import os


class JSONSaver:

    @staticmethod
    def save_into_json_file(list_items: list, filename: str) -> None:
        """
        Сохраняет список элементов в формате JSON в указанный файл.
        :param list_items: Список элементов для сохранения.
        :param filename: Имя файла без расширения, в который нужно сохранить данные.
        :return: None
        """

        root_folder = os.path.dirname(os.path.abspath(__file__))
        json_name = f'{filename}.json'
        full_address = os.path.join(root_folder, 'docs', json_name)

        if os.path.exists(full_address):
            with open(full_address, 'w', encoding='utf-8') as file:
                json.dump(list_items, file, ensure_ascii=False, indent=4)
        else:
            with open(full_address, 'w+', encoding='utf-8') as file:
                json.dump(list_items, file, ensure_ascii=False, indent=4)

        print(f'Добавлено {len(list_items)} элементов в {filename}.json\n')
        print(f'Файл сохранен по адресу: {full_address}\n')
