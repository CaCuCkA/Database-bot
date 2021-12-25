import sqlite3
import datetime


class VehicleDataBase:
    current_date = datetime.datetime.now()  # константа текущего времени

    # Создание базы данных
    def __init__(self, path_to_db="data/vehicle.db"):
        self.path_to_db = path_to_db

    # Чтоб все время не писать connect()
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

    # Создание таблицы автомобилей
    def create_vehicle_table(self):
        sql = """
        CREATE TABLE Vehicles (
        id int NOT NULL,
        driver_id int,
        model varchar(255) NOT NULL, 
        plate_number varchar(255) NOT NULL,
        joiningDate varchar(255),
        editingDate varchar(255) NOT NULL,
        PRIMARY KEY (id)
        );
        """
        self.execute(sql, commit=True)

    # Функция позволяющая добавлять автомобили
    def add_vehicle(self, id: int, model: str, plate_number: str, driver_id=None,
                    joiningDate=current_date, editingDate=current_date):
        joiningDate = self.parsing_date(joiningDate)
        editingDate = self.parsing_date(editingDate)
        sql = "INSERT INTO Vehicles(id, driver_id, model, plate_number, joiningDate, " \
              "editingDate) VALUES(?, ?, ?, ?, ?, ?)"
        parameters = (id, driver_id, model, plate_number, joiningDate, editingDate)
        self.execute(sql, parameters=parameters, commit=True)

    # Функция общего пользования для вывода списка всех автомобилей
    def select_all_vehicles(self):
        sql = "SELECT * FROM Vehicles"
        return self.execute(sql, fetchall=True)

    # Статический метод, который позволяет добавляет бесконечное количество параметров поиска
    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters  # Добавляет AND к каждому парметру, кроме последнего
        ])
        return sql, tuple(parameters.values())

    # Функция общего пользования для вывода конкретного автомобиля с заданными аргументами
    def select_vehicle(self, **kwargs):
        sql = "SELECT * FROM Vehicles WHERE "
        sql, parameters = self.format_args(sql, kwargs)
        return self.execute(sql, parameters, fetchone=True)

    # Функция общего пользования для смены водителя
    def update_driver_id(self, driver_id, id):
        sql = "UPDATE Vehicles SET driver_id=?, editingDate=? WHERE id=?"
        editingDate = self.parsing_date(datetime.datetime.now())
        return self.execute(sql, parameters=(driver_id, editingDate, id), commit=True)

    # Функция общего пользования для смены марки автомобиля
    def update_model(self, model, id):
        sql = "UPDATE Vehicles SET model=?, editingDate=? WHERE id=?"
        editingDate = self.parsing_date(datetime.datetime.now())
        return self.execute(sql, parameters=(model, editingDate, id), commit=True)

    # Функция общего пользования для смены номера автомобиля
    def update_plate_number(self, plate_number, id):
        editingDate = self.parsing_date(datetime.datetime.now())
        sql = "UPDATE Vehicles SET plate_number=?, editingDate=? WHERE id=?"
        return self.execute(sql, parameters=(plate_number, editingDate, id))

    # Функция общего пользования для вывода списка автомобилей С водителем
    def vehicle_with_driver(self):
        vehicles = self.select_all_vehicles()
        final_result = []
        vehicle_dict = {}
        for vehicle in vehicles:
            vehicle_dict[vehicle[0]] = vehicle[1]
        print(vehicle_dict)
        for key, value in vehicle_dict.items():
            if value is not None:
                final_result.append(self.select_vehicle(id=key))
        return final_result

    # Функция общего пользования для вывода списка автомобилей БЕЗ водителем
    def vehicle_without_driver(self):
        vehicles = self.select_all_vehicles()
        final_result = []
        vehicle_dict = {}
        for vehicle in vehicles:
            vehicle_dict[f"{vehicle[0]}"] = vehicle[1]
            print(vehicle_dict)
        for key, value in vehicle_dict.items():
            if value is None:
                final_result.append(self.select_vehicle(id=int(key)))
        return final_result

    # Функция удаляет автомобиль по id.
    def delete_vehicle(self, **kwargs):
        sql = "DELETE FROM Vehicles WHERE "
        sql, parameters = self.format_args(sql, kwargs)
        self.execute(sql, parameters, commit=True, fetchone=True)

    # Функция удаляет все автомобили
    def delete_all(self):
        self.execute("DELETE FROM Vehicles", commit=True)


# Функция логирования. Помогает при тестирование. Отображает какой сейчас этап и где искать ошибку
def logger(statement):
    print(f"""
        _____________________________________________________________________

        Executing:
        {statement}
        _____________________________________________________________________
    """)
