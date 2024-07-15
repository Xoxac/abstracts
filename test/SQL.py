# База данных — это совокупность сущностей (таблиц).
# Каждая сущность может содержать строки или объекты, обладающие некоторыми атрибутами.
# Между сущностями также могут быть выстроены связи — «один к одному», «один ко многим», «многие ко многим».
#___________________________________________________________________________

# CREATE TABLE table_name (
#     field_name TYPE
# );

# Опишем некоторые (пока что не все) атрибуты сущностей базы данных нашего интернет-магазина:

# Сущность «Заказ»
# CREATE TABLE ORDERS (
#     order_id INT AUTO_INCREMENT NOT NULL,
#     time_in DATETIME NOT NULL,
#     time_out DATETIME NOT NULL,
#     cost FLOAT NOT NULL,
#     pickup INT NOT NULL
# );

# AUTO_INCREMENT указывает базе данных, что она должна сама записать сюда
# значение (требуем, чтобы БД сама назначала порядковый номер каждой строке)
# NOT NULL - указываем, что каждое поле должно иметь значение. Иными словами быть ненулевым (not null).
# ORDERS - имя сущности
# order_id INT AUTO_INCREMENT NOT NULL, time_in DATETIME NOT NULL ... - атрибуты сущности

# CREATE TABLE PRODUCTS (
#     product_id INT AUTO_INCREMENT NOT NULL,
#     name CHAR(255) NOT NULL,
#     price FLOAT NOT NULL
# );
# product_id (целочисленный атрибут с автоинкрементом) — уникальный идентификатор товара в каталоге;
# name (строка до 255 символов) — название товара;
# price (число с плавающей точкой) — цена товара.

#___________________________________________________________________________
# Первичный ключ — это атрибут, обеспечивающий уникальность. Как только мы имеем первичный ключ в исходной таблице,
# мы можем создавать связь из другой таблицы, объявляя в ней внешний ключ. Внешний ключ — это атрибут,
# содержащий в себе значение первичного ключа строк таблицы, с которой строится связь.

# CREATE TABLE ORDERS (
#     order_id INT AUTO_INCREMENT NOT NULL,
#     time_in DATETIME NOT NULL,
#     time_out DATETIME,
#     cost FLOAT NOT NULL,
#     pickup INT NOT NULL,
#     PRIMARY KEY (order_id)
# );

# Внешний ключ определяется аналогичным способом. В зависимой таблице (в которой «много» объектов)
# необходимо добавить строку, похожую на ту, что мы использовали для создания первичного ключа:
# FOREIGN KEY (имя_атрибута) REFERENCES Основная_Таблица (первичный_ключ)

# CREATE TABLE ORDERS (
#     order_id INT AUTO_INCREMENT NOT NULL,
#     time_in DATETIME NOT NULL,
#     time_out DATETIME,
#     cost FLOAT NOT NULL,
#     pickup INT NOT NULL,
#     PRIMARY KEY (order_id)
#     FOREIGN KEY (staff) REFERENCES STAFF (staff_id)
# );

# _______________________________________________________________________
# При помощи SQL создайте таблицу PRODUCTS_ORDERS, которая должна:
#
# Содержать атрибут product_order_id, который предполагается целочисленным, автоматически
# увеличивающимся на 1 и тем самым должен стать первичным ключом этой таблицы.
# Содержать атрибут product, который ссылается на первичный ключ таблицы Products.
# Содержать атрибут in_order, который ссылается на первичный ключ таблицы Orders.
# Содержать атрибут amount, который определяет количество конкретного продукта в заказе.
# Мы предполагаем, что это целое число.
#
# CREATE TABLE PRODUCTS_ORDERS (
#     product_order_id INT AUTO_INCREMENT NOT NULL,
#     product INT NOT NULL,
#     in_order INT NOT NULL,
#     amount INT NOT NULL,
#
#     PRIMARY KEY (product_order_id),
#     FOREIGN KEY (product) REFERENCES PRODUCTS (product_id),
#     FOREIGN KEY (in_order) REFERENCES ORDERS (order_id)
# );
#___________________________________________________________________________

# Фреймворк Django как раз и реализует в себе механизм ORM, чтобы иметь возможность представлять сущности
# в виде классов, а объекты этих сущностей (строки таблиц) — в виде экземпляров этих классов.
# Например, чтобы создать сущности для базы данных интернет-магазина, мы можем написать следующие заголовки классов:

# from django.db import models  # импорт

# class Order(models.Model):  # наследуемся от класса Model
#     pass

# class Product(models.Model):
#     pass

# class Staff(models.Model):
#     pass

# class ProductOrder(models.Model):
#     pass

# В том же модуле, где хранится класс Model, от которого мы наследуем все модели, можно найти ещё несколько классов,
# позволяющих определить поля модели. Эти поля DjangoORM самостоятельно трансформирует в атрибуты сущностей
# уже в базе данных.
# object_id = models.AutoField() # Целочисленное поле, которое автоматически увеличивается для каждой строки. Это аналог AUTOINCREMENT
# boolean = models.BooleanField(default = False)
# small_string = models.CharField(max_length = 64,
#                                 default = "Default value") # Строковый тип. Используется, как правило, для небольших строковых данных.
# some_data = models.DateField(auto_now_add = True) # Поле, предназначенное для хранения даты. В Python оно представлено объектом datetime.date
# personal_email = models.EmailField() # при сохранении объекта, данные проверяются на соответствие формату anyone@anywhere.com
# ...

# файл models.py
# Переделываем SQL таблицы:
# было:
# CREATE TABLE PRODUCTS (
#     product_id INT AUTO_INCREMENT NOT NULL,
#     name CHAR(255) NOT NULL,
#     price FLOAT NOT NULL
# );
# делаем:
# from django.db import models

# class Product(models.Model):
#     name = models.CharField(max_length = 255)
#     price = models.FloatField(default = 0.0)

# class Staff(models.Model):
#     full_name = models.CharField(max_length = 255)
#     position = models.CharField(max_length = 255)
#     labor_contract = models.IntegerField()

