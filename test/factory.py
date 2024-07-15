# Шаблон проектирования "Фабрика" – это паттерн, который позволяет создавать объекты различных классов через
# единый интерфейс. Это помогает избежать кросс-импорта, делая код более модульным и гибким.









# Определяется интерфейс продукта: Создается абстрактный класс или интерфейс, который определяет общие
# характеристики создаваемых объектов.
class ElectronicDevice(object):
    def turn_on(self):
        pass

    def turn_off(self):
        pass

# Реализация конкретных продуктов: Создаются классы, которые наследуют от абстрактного класса или
# интерфейса продукта и реализуют его специфическую функциональность.
class Smartphone(ElectronicDevice):
    def turn_on(self):
        print("Включаю смартфон")

    def turn_off(self):
        print("Выключаю смартфон")

class Tablet(ElectronicDevice):
    def turn_on(self):
        print("Включаю планшет")

    def turn_off(self):
        print("Выключаю планшет")

class Laptop(ElectronicDevice):
    def turn_on(self):
        print("Включаю ноутбук")

    def turn_off(self):
        print("Выключаю ноутбук")

# Фабричный класс: Создается класс фабрики, который отвечает за создание объектов продуктов. Этот класс
# содержит метод createProduct(), который принимает параметр, указывающий тип создаваемого продукта.
class ElectronicDeviceFactory(object):
    @staticmethod
    def create_device(device_type):
        if device_type == "смартфон":
            return Smartphone()
        elif device_type == "планшет":
            return Tablet()
        elif device_type == "ноутбук":
            return Laptop()
        else:
            raise ValueError(f"Неизвестный тип устройства: {device_type}")

# Создание объектов: Клиентский код взаимодействует только с фабричным классом. Для создания объекта
# продукта клиентский код вызывает метод createProduct(), передавая ему желаемый тип продукта. Фабричный класс,
# в свою очередь, создает объект соответствующего класса продукта и возвращает его клиенту.

# Используем фабрику:
factory = ElectronicDeviceFactory()
device = factory.create_device("smartphone")
device.turn_on()
device.turn_off()

device = factory.create_device("laptop")
device.turn_on()
device.turn_off()
