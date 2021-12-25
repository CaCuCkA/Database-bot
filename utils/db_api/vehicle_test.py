from utils.db_api.vehicle_base import VehicleDataBase

db = VehicleDataBase()


# КОМАНДЫ ДЛЯ ТЕСТИРОВАНИЯ
# create_vehicle_table() - создает таблицу автомобилей
# add_vehicle() - добавляет автомобиль
# select_vehicle() - выбирает конкретный автомобиль
# select_all_vehicles() - выделяет все автомобили
# update_driver_id() - добавляет/убирает водителя
# update_model() - изменяет марку автомобиля
# update_plate_number() - изменяет номер автомобиля
# vehicle_with_driver() - выводит список автомобилей С водителем
# vehicle_without_driver() - выводит список автомобилей БЕЗ водителей
# delete_vehicle() - удаляет конретный автомобиль
# delete_all() - удаляет все автомобили

# БЕТА ТЕСТ РАБОТЫ БАЗЫ ДАННЫХ
def driver_test():
    # Созание таблицы данных
    # db.create_vehicle_table() закоментил, так как будет ошибка при повторном создании
    # Выделим все автомобили, которые у нас есть, для проверки количества до регестрации новых автомобилей
    vehicles = db.select_all_vehicles()
    print(f"Количество машин до добавление пользователем {vehicles}")
    # Регестрация 5 новых автомобилей
    db.add_vehicle(id=1, model="Volvo", plate_number="AA 2031 CB")
    db.add_vehicle(id=2, model="Mercedes", plate_number="AA 2031 CB")
    db.add_vehicle(id=3, model="Volkswagen", driver_id=14, plate_number="AA 2031 CB")
    db.add_vehicle(id=4, model="Tesla", driver_id=23, plate_number="AA 2031 CB")
    db.add_vehicle(id=5, model="Ferrari", plate_number="AA 2031 CB")
    # Проверка их добавления
    vehicles = db.select_all_vehicles()
    print(f"Количество машин после добавление пользователем {vehicles}")
    # Добавление водителя
    db.update_driver_id(driver_id=12, id=1)
    vehicle = db.select_vehicle(id=1)
    print(f"Добавление айди водителя в машину с id = 1: {vehicle}")
    # Изминение марки автомобиля
    db.update_model(id=5, model="Lamborghini")
    vehicle = db.select_vehicle(id=5)
    print(f"Изминение модели автомобиля с id = 5: {vehicle}")
    # Изминение автомобильного номера
    db.update_plate_number(id=2, plate_number="CB 1256 OK")
    vehicle = db.select_vehicle(id=2)
    print(f"Изминение номера автомобиля с id = 2: {vehicle}")
    # Выведим список автомобилей С водителем
    vehicles = db.vehicle_with_driver()
    print(vehicles)
    # Выведим список автомобилей БЕЗ водителя
    vehicles = db.vehicle_without_driver()
    print(vehicles)
    # Удаление конкретного автомобиля
    db.delete_vehicle(id=3)
    vehicles = db.select_all_vehicles()
    print(f"Список автомобилей после удаления автомобиля с id = 3: {vehicles}")
    # Удаление всех автомобилей
    db.delete_all()
    vehicles = db.select_all_vehicles()
    print(f"База данных после удаление всех автомобилей: {vehicles}" )


db.delete_all()
driver_test()
