import sqlite3
import datetime


class DriverDataBase:
    current_date = datetime.datetime.now()  # константа текущего времени

    # Создание базы данных
    def __init__(self, path_to_db="data/drivers.db"):
        self.path_to_db = path_to_db

    # Чтобы не писать сonnection()
    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    # Подключение SQLite
    def execute(self, sql: str, parameters: tuple = None, fetchone=False,
                fetchall=False, commit=False):
        if not parameters:
            parameters = tuple()
        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchone:
            data = cursor.fetchone()
        if fetchall:
            data = cursor.fetchall()

        return data

    # Метод представления даты day-month-year
    @staticmethod
    def parsing_date(date: datetime.datetime):
        year = '{:02d}'.format(date.year)
        month = '{:02d}'.format(date.month)
        day = '{:02d}'.format(date.day)
        return '{}-{}-{}'.format(day, month, year)

    # Создание таблицы водителей
    def create_drivers_table(self):
        sql = """
        CREATE TABLE Drivers (
        id int NOT NULL,
        first_name varchar(255) NOT NULL, 
        last_name varchar(255) NOT NULL, 
        joiningDate varchar(255) NOT NULL, 
        editingDate varchar(255), 
        PRIMARY KEY (id)
        );
        """
        self.execute(sql, commit=True)

    # Функция позволяющая добавлять водителей.
    def add_driver(self, Id: int, first_name: str, last_name: str, joiningDate=current_date,
                   editingDate=current_date):
        joiningDate = self.parsing_date(joiningDate)
        editingDate = self.parsing_date(editingDate)
        sql = "INSERT INTO Drivers(id, first_name, last_name, joiningDate, editingDate) VALUES(?, ?, ?, ?, ?)"
        parameters = (Id, first_name, last_name, joiningDate, editingDate)
        self.execute(sql, parameters=parameters, commit=True)

    # Функция общего пользования для вывода списка всех водителей
    def select_all_drivers(self):
        sql = "SELECT * FROM Drivers"
        return self.execute(sql, fetchall=True)

    # Статический метод, который позволяет добавляет бесконечное количество параметров поиска
    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters  # Добавляет AND к каждому парметру, кроме последнего
        ])
        return sql, tuple(parameters.values())

    # Функция общего пользования для вывода конкретного пользователя с заданными аргументами
    def select_driver(self, **kwargs):
        sql = "SELECT * FROM Drivers WHERE "
        sql, parameters = self.format_args(sql, kwargs)
        return self.execute(sql, parameters, fetchone=True)

    # Функция общего пользования для смены имени водителя
    def update_first_name(self, first_name, Id):
        editingDate = self.parsing_date(datetime.datetime.now())
        sql = "UPDATE Drivers SET first_name=?, editingDate=? WHERE Id=?"
        return self.execute(sql, parameters=(first_name, editingDate, Id), commit=True)

    # Функция общего пользования для смены фамилии водителя
    def update_last_name(self, last_name, Id):
        editingDate = self.parsing_date(datetime.datetime.now())
        sql = "UPDATE Drivers SET last_name=?, editingDate=? WHERE id=?"
        return self.execute(sql, parameters=(last_name, editingDate, Id), commit=True)

    # Для разроботчиков, чтоб проверить возможности сортировки
    # Можно использовать для изминения даты "регестрации" пользователя
    def __update_joining_date(self, joiningDate, Id):
        sql = "UPDATE Drivers SET joiningDate=? WHERE id=?"
        return self.execute(sql, parameters=(joiningDate, Id), commit=True)

    # Статическая функция позволяющая переводить строку в целые числа day, month, year,
    # которые потом переводяться в количество дней и выводятся суммой.
    @staticmethod
    def date_opening(date: str):
        parcing_list = list(map(int, date.split("-")))
        return parcing_list[0] + parcing_list[1] * 30 + parcing_list[-1] * 365

    # Функция разделения по дате. Выводить всех водителей, которые зарегестрировались ДО определенной даты
    def drivers_filter_created_before(self, date: str):
        Drivers = self.select_all_drivers()
        final_result = []
        drivers_dict = {}
        for driver in Drivers:
            drivers_dict[f"{driver[0]}"] = driver[3]
        print(drivers_dict)
        for key, value in drivers_dict.items():
            if self.date_opening(value) < self.date_opening(date):
                final_result.append(self.select_driver(id=int(key)))
            return final_result

    # Функция разделения по дате. Выводить всех водителей, которые зарегестрировались ПОСЛЕ определенной даты
    def drivers_filter_created_after(self, date: str):
        Drivers = self.select_all_drivers()
        final_result = []
        drivers_dict = {}
        for driver in Drivers:
            drivers_dict[f"{driver[0]}"] = driver[3]
        print(drivers_dict)
        for key, value in drivers_dict.items():
            if self.date_opening(value) > self.date_opening(date):
                final_result.append(self.select_driver(id=int(key)))
        return final_result

    # Функция удаляет водителя по id
    def delete_driver(self, **kwargs):
        sql = "DELETE FROM Drivers WHERE "
        sql, parameters = self.format_args(sql, kwargs)
        self.execute(sql, parameters, commit=True, fetchone=True)

    # Функция удаляет всех пользователей
    def delete_all(self):
        self.execute("DELETE FROM Drivers", commit=True)


# Функция логирования. Помогает при тестирование. Отображает какой сейчас этап и где искать ошибку
def logger(statement):
    print(f"""
        _____________________________________________________________________

        Executing:
        {statement}
        _____________________________________________________________________
    """)
