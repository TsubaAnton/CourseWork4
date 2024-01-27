from abc import ABC, abstractmethod
import requests


class AbstractAPI(ABC):
    """
    Абстрактный класс для работы с API вакансий.
    """

    @abstractmethod
    def get_vacancies(self, text):
        """
        Получает список вакансий по заданному текстовому запросу.
        """
        pass

    @abstractmethod
    def filter_vacancies(self, text):
        """
        Фильтрует список вакансий по заданному текстовому запросу.
        """
        pass


class Superjob(AbstractAPI):
    """
    Класс для работы с API SuperJob и получения вакансий.
    """

    def get_vacancies(self, text, page=5):
        """
        Получает список вакансий SuperJob по заданному текстовому запросу.
        """
        headers = {"X-Api-App-Id": "v3.r.138107070.c3e1b4d98e4dee6e4a95253ecb3add9a9ba36cb3.1a11e7358ed4747ceff965fd41f803f4874002ab"}
        vacancies = []
        for i in range(page):
            params = {"keywords": text, "page": i}
            vacancies_one_page = requests.get("https://api.superjob.ru/2.0/vacancies/", params=params, headers=headers).json()["objects"]
            vacancies.extend(vacancies_one_page)
        return vacancies

    def filter_vacancies(self, text):
        """
        Фильтрует список вакансий SuperJob по заданному текстовому запросу.
        """
        vacancies = self.get_vacancies(text)
        vacancies_filter = []
        for vacancy in vacancies:
            vacancies_filter.append({
                "name": vacancy["profession"],
                "url": vacancy["link"],
                "salary_from": vacancy["payment_from"],
                "salary_to": vacancy["payment_to"],
                "description": vacancy["candidat"]
            })
        return vacancies_filter


class HeadHunter(AbstractAPI):
    """
    Класс для работы с API HeadHunter и получения вакансий.
    """

    def get_vacancies(self, text):
        """
        Получает список вакансий HeadHunter по заданному текстовому запросу.
        """
        page = 0
        params = {
            'text': f'NAME:{text}',
            'area': 1,
            'page': page,
            'per_page': 100
        }
        vacancies = requests.get('https://api.hh.ru/vacancies', params).json()
        return vacancies.get('items', [])

    def filter_vacancies(self, text):
        """
        Фильтрует список вакансий HeadHunter по заданному текстовому запросу.
        """
        vacancies = self.get_vacancies(text)
        vacancies_filter = []
        for vacancy in vacancies:
            salary_info = vacancy.get("salary")

            if salary_info is not None:
                salary_from = salary_info.get("from", 0)
                salary_to = salary_info.get("to", 0)
            else:
                salary_from = 0
                salary_to = 0

            vacancies_filter.append({
                "name": vacancy.get("name", ""),
                "url": vacancy.get("url", ""),
                "salary_from": salary_from,
                "salary_to": salary_to,
                "description": vacancy.get("snippet", {}).get("requirement", "")
            })

        return vacancies_filter

