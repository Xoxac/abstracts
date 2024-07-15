# create virtual environment
# python -m venv <name>
# venv\scripts\activate

# install django
# pip install django

# create blank project
# django-admin startproject <name_of_project>

# run server
# cd <name_of_project>
# python manage.py runserver

# go to browser
# http://127.0.0.1:8000/

# set up migrations (files that tells to database what info will be stored on it)
# project/settings.py
# python manage.py migrate


# Начнём с простого. Научим наше приложение показывать пользователю простейшие веб-странички на чистом HTML
# с помощью встроенного инструмента — Django Flatpages. И для этого необходимо внести изменения
# как в back-end, так и в front-end

# create admin
# python manage.py createsuperuser
# now DB has info that admin exists and has name and password
# way "http://127.0.0.1:8000/admin/" automatically created in urls.py
# urlpatterns = ['admin/', admin.site.urls] значит, что за то, что увидит пользователь, введя после адреса /admin,
#       отвечает приложение admin
# python manage.py runserver
# go to http://127.0.0.1:8000/admin/

# добавим в наш проект новые приложения для работы с плоскими страничками - они изначально отключены
# settings.py - INSTALLED_APPS - add 'django.contrib.sites', 'django.contrib.flatpages'
# и добавим переменную SITE_ID = 1
# и 'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware' to MIDDLEWARE

# поскольку мы добавили новое приложение, нужно указать ссылку, по которой они доступны
# urls.py - from django.urls import path, include (добавить)
# в urlpatterns добавим ('pages/', include('django.contrib.flatpages.urls'))

# пишем первую статическую страницу
# В директории с файлом manage.py нужно создать файл по следующему пути: templates/flatpages/default.html
# fill html code:
# <!DOCTYPE html>
# <html>
# <head>
# <title>{{ flatpage.title }}</title>    # {{ flatpage.title }} передаст текст из панели flatpages на сайте
# </head>
# <body>
# {{ flatpage.content }}    # передаст текст из панели flatpages на сайте
# </body>
# </html>
# http://127.0.0.1:8000/admin/
# flat pages - add - fill all
# error "templateDoNotExist" значит что не находит шаблон.
# import os, Указываем путь в
# settings.py - TEMPLATES - DIRS - os.path.join(BASE_DIR, 'templates')

# add page
# templates - new html - 'about'
# в панели внизу указать новый темплейт
# теперь по ссылке about другой шаблон

# Несмотря на то, что после выполнения миграций, в админке появились наши модели FlatPages и Sites,
# в них по умолчанию зарегистрированы не все поля. Для того чтобы мы могли видеть такие поля, как
# «Позволить комментировать» или «Отображение только зарегистрированным пользователям», нам надо
# зарегистрировать класс, наследуемый от FlatPageAdmin, но добавить в него нужные нам
# поля (вспоминаем полиморфизм) и наследование.

# Создадим файл fpages/admin.py со следующим содержанием:
# from django.contrib import admin
# from django.contrib.flatpages.admin import FlatPageAdmin
# from django.contrib.flatpages.models import FlatPage
# from django.utils.translation import gettext_lazy as _
#
#
# Define a new FlatPageAdmin
# class FlatPageAdmin(FlatPageAdmin):
#     fieldsets = (
#         (None, {'fields': ('url', 'title', 'content', 'sites')}),
#         (_('Advanced options'), {
#             'classes': ('collapse',),
#             'fields': (
#                 'enable_comments',
#                 'registration_required',
#                 'template_name',
#             ),
#         }),
#     )
#
#
# Re-register FlatPageAdmin
# admin.site.unregister(FlatPage)
# admin.site.register(FlatPage, FlatPageAdmin)

# Впишите новое приложение Fpages в настройках
# Появились новые поля Enable comments и Registration required помимо уже изученного нами Template name


# Если на сайте был бы миллион различных страниц, то, поменяв шапку, пришлось бы менять её во всех шаблонах по очереди.
# Это неудобно, конечно же, но вот тут к нам и приходят на помощь специальные теги шаблонизатора Django
# в body вставляем {% include '<путь к html странице>' %} и на это место идет весь код с той страницы
# либо вставляем {% extends '<путь к html странице>' %} и теги {% block content %} и {% endblock content %}
# написали в шаблоне-родителе блок, например, {% block content %}, закрыли блок {% enblock content %}.
# В шаблоне-наследнике теперь можно внутри этого блока писать содержимое страницы


# Bootstrap — это библиотека для упрощения работы с HTML- и CSS-кодом.
# Берем готовые шаблоны - в любом поиске написать запрос «bootstrap free templates»
# архив с готовыми шаблонами CSS-файлами и т. д., нам надо распаковать его в директорию static/
# (папку static надо будет создать самостоятельно в той же папке, что и manage.py)
# Из всего нам потребуется только файл index.html и папка css, в которой как раз-таки будут лежать наши стили.
# assets и js можно спокойно удалить, они нам пока не понадобятся. В assets лежит иконка,
# а в js — пустой скрипт (так как наша страница статична).
# И в настройках добавить строчку в самом конце, для подгрузки стилей из папки static :
# STATICFILES_DIRS = [BASE_DIR / "static"]

# Во-первых, содержимое файла index.html нам надо скопировать в шаблон default.html, и смело можем его затем удалять.
# Первым делом нас интересует блок head. Подгружаем стили с помощью команды {% load static %}.
# Удаляем строчку, которая отвечает за иконку: <link rel="icon" type="image/x-icon" href="assets/favicon.ico" />
# И изменяем строчку, которая отвечает за подгрузку наших стилей:
# <link href="css/styles.css" rel="stylesheet" />  на <link href="{% static 'css/styles.css' %}" rel="stylesheet" />

# Но информация пока ещё не такая, как нам нужна, для этого стоит обратиться к блоку body в нашем HTML-файле.
# Для начала в самом его конце удалим строчки, отвечающие за подгрузку JS
# (хоть у нас всё и работает с ними, но код должен быть чистым).

# После обратимся к месту, которое разработчики стиля указали как <!--Page content-->,
# что говорит нам о том, что тут текст страницы ниже шапки. И также удалим, у нас будет свой контент.
# Вставим после Page content данную структуру:
# <div class="container">
#    <div class="row">
#        <div class="col-lg-12 text-center">
#            {% block content %}
#            {{ flatpage.content }}
#            {% endblock content %}
#        </div>
#    </div>
# </div>

# Теперь изменим шапку страницы.
# Для этого нам потребуется место, которое в коде указано как Responsive navbar.
# Вставим туда вместо исходного кода этот:
# <nav class="navbar navbar-expand-lg navbar-dark bg-dark static-top">
#    <div class="container">
#        <a class="navbar-brand" href="#">Django flatpages</a>
#        <button class="navbar-toggler" type="button" data-toggle="collapse"
#                data-target="#navbarResponsive"
#                aria-controls="navbarResponsive" aria-expanded="false"
#                aria-label="Toggle navigation">
#            <span class="navbar-toggler-icon"></span>
#        </button>
#        <div class="collapse navbar-collapse" id="navbarResponsive">
#            <ul class="navbar-nav ml-auto">
#                <li class="nav-item active">
#                    <a class="nav-link" href="#">Home
#                        <span class="sr-only">(current)</span>
#                    </a>
#                </li>
#                <li class="nav-item">
#                    <a class="nav-link" href="/about/">About</a>
#                </li>
#                <li class="nav-item">
#                    <a class="nav-link" href="/contacts/">Contact</a>
#                </li>
#            </ul>
#        </div>
#    </div>
# </nav>




