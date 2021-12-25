from utils.db_api.drivers_base import DriverDataBase

db = DriverDataBase()


# КОМАНДЫ ДЛЯ ТЕСТИРОВАНИЯ
# create_drivers_table() - создает таблицу водителей
# add_driver() - добавляет водителей
# select_driver() - выбирает конкретного водителя
# select_all_drivers() - выделяет всех водителей
# update_last_name() - изменяет фамилию
# update_first_name() - изменяет имя
# __update_joining_date() - изменяет дату регестрации !ЧИСТО ДЛЯ ТЕСТИРОВКИ, ПРИВАТНАЯ ФУНКЦИЯ!
# drivers_filter_created_before() - выводит список зарегестрировавщихся ДО определенной даты
# drivers_filter_created_after() - выводит список зарегестрировавщихся ПОСЛЕ определенной даты
# delete_driver() - удаляет конретного водителя
# delete_all() - удаляет всех водителей

# БЕТА ТЕСТ РАБОТЫ БАЗЫ ДАННЫХ
def test():
    # Созание таблицы данных
    # db.create_drivers_table() закоментил, так как будет ошибка при повторном создании
    # Выделим всех водителей, которые у нас есть, для проверки количества до регестрации новых водителей
    drivers = db.select_all_drivers()
    print(f"До добавления водителей: {drivers}")
    # Регестрация 5 новых водитлей
    db.add_driver(6, 'George', 'uni')
    db.add_driver(2, 'Yak', 'Yakov')
    db.add_driver(3, 'Jack', 'Jackov')
    db.add_driver(4, 'Ivan', 'Ivanov')
    db.add_driver(5, 'Alex', 'Alexov')
    # Проверка их добавления
    drivers = db.select_all_drivers()
    print(f"После добавления водителей: {drivers}")
    # Изминение имени у водителя
    db.update_first_name("Sasha", 3)
    driver = db.select_driver(first_name="Sasha", id=3)
    print(f"""Изминение имени с Jack на  Sasha: {driver}""")
    # Изминение фамилии у водителя
    db.update_last_name("Yakovkin", 5)
    print(f"Изминение фамилии с Alexov на Yakovkin: {db.select_driver(id=5)}")
    # Исправление даты регестрации для тестировки функций
    db._DriverDataBase__update_joining_date(joiningDate='13-09-2016', Id=6)
    # Вывод водителей созданых ДО n-ой даты
    users = db.drivers_filter_created_before('19-12-2021')
    print(users)
    # Вывод водителей созданых ПОСЛЕ n-ой даты
    users = db.drivers_filter_created_after('19-12-2021')
    print(users)
    # Удаление конкретного водителя с таблицы
    db.delete_driver(id=4)
    drivers = db.select_all_drivers()
    print(f"Изминение после удаления водителя с id = 4: {drivers}")
    # Удаление всех водителей с таблицы
    db.delete_all()
    drivers = db.select_all_drivers()
    print(f"Удаление всех водителей с таблицы: {drivers}")


db.add_driver(6, 'George', 'uni')
user = db.select_driver(id=6)
print(type(user))
# test()
