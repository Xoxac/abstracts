# Jinja - это модуль для обработки и преобразования текстовых шаблонов
import option
from jinja2 import *

# с помощью класса Template, импортированного из Jinja2, создаем шаблон:
name = 'Fedor'
tm = Template('Hi {{ name }}') # создаем экземпляр класса Template на основе текстового шаблона Hi {{ name }}, который
                               # вместо name подставляет значение.
msg = tm.render(name=name)     # для этого используется метод render класса Template, принимающий именованный
                               # параметр name со значением переменной name и возвращающий готовую строку.
print(msg)

msg2 = f'Hi {name}'            # выглядит при выводе так же, поэтому в простых случаях использовать f строки

print(msg2)

# {%%} - спецификатор шаблона
# {{}} - выражение для вставки конструкций Python в шаблон
# {##} - блок комментариев
# ### - строковый комментарий


# -- использование {{ }} в шаблонах --

name = 'Xoxa'
age = 39

tm = Template('I am {{ a }} years old and my name is {{ n }}')
msg = tm.render(n=name, a=age)

print(msg)

tm = Template('I am {{ a*2 }} years old and my name is {{ n.upper() }}') # можно впихнуть любые выражения
msg = tm.render(n=name, a=age)

print(msg)

# усложним задачу и представим человека как экземпляр класса Person:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

per = Person('Vas', 33)

tm = Template('I am {{ p.age }} years old and my name is {{ p.name }}')
msg = tm.render(p = per)

print(msg)


# -- Экранирование и блоки raw, for, if--
# например, хотим фрагмент шаблона никак не преобразовывать (то есть, чтобы отображалось {{ name }} и не заменялось.
# Для этого есть блок {%raw%} ... {%endraw%}:

data = '''Модуль Jinja вместо определения {{ name }} подставляет следующее значение'''

tm = Template(data)
msg = tm.render(name='Xoxa')

print(msg)

data = '''{%raw%}Модуль Jinja вместо определения {{ name }} подставляет следующее значение{%endraw%}'''

tm = Template(data)
msg = tm.render(name='Xoxa')

print(msg)

link = '''В HTML ссылки определяются так: <a href="#">Ссылка</a>'''

tm = Template(link)
msg = tm.render()

print(msg)

# если этот код сохранить как html файл, то код <a href="#">Ссылка</a> заменится на ссылку.
# чтобы этого избежать, нужно экранирование (флаг e после |):

tm = Template("{{ link | e}}")
msg = tm.render(link=link)

print(msg) # теперь теги заменены на кодировки символов, но в html файле будет строка <a href="#">Ссылка</a>


# блок {%for<выражение>-%} <повторяемый фрагмент> {%endfor%}
# позволяет сформировать список на основе любого итерируемого объекта

cities = [{'id': 1, 'city': 'Moscow'},
          {'id': 5, 'city': 'Tver'},
          {'id': 7, 'city': 'Minsk'},
          {'id': 8, 'city': 'Smolensk'},
          {'id': 11, 'city': 'Kaluga'}]

# мы хотим на основе списка городов сформировать список для html документа с помощью тега select
link = '''<select name="cities">
{% for c in cities %}<option value="{{c['id']}}">{{c['city']}}</option>
{% endfor %}
</select>'''

tm = Template(link)
msg = tm.render(cities=cities)

print(msg)

# {%if<условие>%}<фрагмент при истинности условия>{%endif%} - блок проверки условия
link = '''<select name="cities">
{% for c in cities -%}
{% if c.id > 6 -%}
    <option value="{{c['id']}}">{{c['city']}}</option>
{% else -%}
    {{c['city']}}
{% endif -%}
{% endfor -%}
</select>'''

tm = Template(link)
msg = tm.render(cities=cities)

print(msg) # Москва и Тверь имеют id < 6, поэтому они не были заключены в тег options


# -- фильтры и макросы --
# например, нужно вывести суммарную стоимость всех авто из списка:
cars = [
    {'model': 'Audi', 'price': 23000},
    {'model': 'Skoda', 'price': 20000},
    {'model': 'Volvo', 'price': 27000},
    {'model': 'BMW', 'price': 33000}
]

# Пишем такой шаблон:
tpl = "Суммарная цена автомобилей {{ cs | sum(attribute='price') }}"
tm = Template(tpl)
msg = tm.render(cs = cars)
print(msg)
# код означает, что фильтр sum будет вызываться для коллекции cs и суммирование будет производиться по атрибуту price

digs = [1, 2, 3, 4, 5]
tpl = "Random digit: {{ d | random }}"
tm = Template(tpl)
msg = tm.render(d=digs)
print(msg)

tpl = "Random digit: {{ d | replace(2, 0) }}"
tm = Template(tpl)
msg = tm.render(d=digs)
print(msg)

# -- блок filter
# {{% filter<имя фильтра>%}<фрагмент для применения фильтра>{%endfilter%}
persons = [
    {"name": "Alex", "old": 18, "weight": 78.5},
    {"name": "Nik", "old": 28, "weight": 82.2},
    {"name": "Ivan", "old": 33, "weight": 94.0},
]

tpl = '''
{%- for u in users -%}
{% filter upper %}{{u.name}}{% endfilter %}
{% endfor %}
'''
tm = Template(tpl)
msg = tm.render(users = persons)
print(msg)

# список всех фильтров: https://jinja.palletsprojects.com/en/2.11.x/templates/

# -- macro
# хотим несколько полей input в html документе.
# пишем ключевое слово macro, имя макроопределения input и параметры, если нужны.
# теперь можем использовать макрос много раз
html = '''
{% macro input(name, value='', type='text', size=20) -%}
    <input type="{{ type }}" name="{{ name }}" value="{{ value|e }}" size="{{ size }}">
{%- endmacro %}

<p>{{ input('username')}}
<p>{{ input('email')}}
<p>{{ input('password')}}
'''

tm = Template(html)
msg = tm.render()
print(msg)

# -- call - вложенные макросы
# хотим сформировать список имен, каждое из которых имеет список параметров (вес и возраст)
# в Html он выглядит так:
# <ul>
# <li>Alex
#     <ul>
#     <li>age:
#     <li>weght: 78.5
# <li>Nik ...

# создадим макроопределение, создающее html список имен:
html = '''
{% macro list_users(list_of_user) -%}
<ul>
{% for u in list_of_user -%}
    <li>{{u.name}}
{%- endfor %}
</ul>
{%- endmacro %}

{{list_users(users)}}
'''

tm = Template(html)
msg = tm.render(users=persons)
print(msg)

# добавим для каждого вложенный список, добавив после {{u.name}} метод {{caller(u)}},
# вместо которого будет вставляться блок call:

html = '''
{% macro list_users(list_of_user) -%}
<ul>
{% for u in list_of_user -%}
    <li>{{u.name}} {{caller(u)}}
{%- endfor %}
</ul>
{%- endmacro %}

{% call(user) list_users(users) %}
    <ul>
    <li>age: {{user.old}}
    <li>weight: {{user.weight}}
    </ul>
{% endcall -%}}
'''
tm = Template(html)
msg = tm.render(users=persons)
print(msg)


# -- include --
# страница обычно делится на header, content и footer, что означает, что можно
# создать 3 файла и потом соединить их с помощью include
# создали в templates 3 файла: footer, header, page. В page include footer и header.
# теперь в каждую страницу их вставляем и все.


# -- наследование (расширение) шаблонов --
# создаем ex_main с кодом.
# используем именованные блоки {% block title %}{% endblock %} и {% block content %}{% endblock %}
# создаем шаблон about.htm, первой строчкой пишем {% extends 'ex_main.htm' %} - то есть, имя шаблона, который мы расширяем.

# file_loader = FileSystemLoader('templates')
# env = Environment(loader=file_loader)
#
# template = env.get_template('about.htm')
#
# output = template.render()
# print(output)