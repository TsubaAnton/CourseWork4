import json
from vacancy import Vacancy


class JSONSaver:
    """
    Класс для сохранения и загрузки вакансий в формате JSON.

    Атрибуты:
    - file_path (str): Путь к файлу JSON.
    """
    def __init__(self, file_path):
        """
        Инициализирует объект JSONSaver.
        """
        self.file_path = file_path

    def write_vacancies(self, vacancies):
        """
        Записывает вакансии в файл.
        """
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(vacancies, file, ensure_ascii=False, indent=4)

    def read_vacancies(self):
        """
        Загружает вакансии из файла.
        """
        with open(self.file_path, encoding="utf-8") as file:
            vacancies = json.load(file)
        list_vacancies = []
        for vacancy in vacancies:
            list_vacancies.append(Vacancy(vacancy["name"],
                                          vacancy["url"],
                                          vacancy["salary_from"],
                                          vacancy["salary_to"],
                                          vacancy["description"]))
        return list_vacancies

    def add_vacancy(self, vacancy):
        """
        Добавляет новую вакансию в файл.
        """
        vacancies = self.read_vacancies()
        vacancies.append(vacancy)
        self.write_vacancies(vacancies)

    def remove_vacancy(self, vacancy_url):
        """
        Удаляет вакансию по URL из файла.
        """
        vacancies = self.read_vacancies()
        filtered_vacancies = [v for v in vacancies if v["url"] != vacancy_url]
        self.write_vacancies(filtered_vacancies)

    def save_vacancies(self, vacancies):
        """
        Сохраняет вакансии в формате JSON.
        """
        with open(self.file_path, 'w', encoding='utf-8') as file:
            json.dump([v.as_dict() for v in vacancies], file, ensure_ascii=False, indent=2)

    def filter_vacancies_by_salary(self, min_salary, max_salary):
        """
        Фильтрует вакансии по зарплате.
        """
        with open(self.file_path, 'r', encoding='utf-8') as file:
            all_vacancies = json.load(file)

        filtered_vacancies = [
            Vacancy(v["name"], v["url"], v["salary_from"], v["salary_to"], v["description"])
            for v in all_vacancies
            if min_salary <= (v["salary_from"] or 0) <= max_salary
        ]

        return filtered_vacancies
