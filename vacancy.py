class Vacancy:
    """
    Класс, представляющий вакансию.

    Атрибуты:
    - name (str): Название вакансии.
    - url (str): Ссылка на вакансию.
    - salary_from (float): Минимальная зарплата.
    - salary_to (float): Максимальная зарплата.
    - description (str): Описание вакансии.
    """
    def __init__(self, name, url, salary_from, salary_to, description):
        """
        Инициализирует объект Vacancy.
        """
        self.name = name
        self.url = url
        self.salary_from = salary_from if salary_from is not None else 0
        self.salary_to = salary_to if salary_to is not None else 0
        self.description = description

    def __str__(self):
        """
        Возвращает строковое представление вакансии.
        """
        return f"""Название вакансии: {self.name}
Ссылка: {self.url}
Зарплата от {self.salary_from} до {self.salary_to}"""

    def __lt__(self, other):
        """
        Сравнивает вакансии по минимальной зарплате для сортировки по возрастанию.
        """
        return self.salary_from if self.salary_from is not None else 0 > other.salary_from if other.salary_from is not None else 0  # метод по возрастанию

    def as_dict(self):
        """
        Преобразует объект Vacancy в словарь.
        """
        return {
            "name": self.name,
            "url": self.url,
            "salary_from": self.salary_from,
            "salary_to": self.salary_to,
            "description": self.description
        }