# OZIMIZ.KAZ

## Установка

Первое, что нужно сделать, это клонировать репозиторий:

sh
$ git clone https://github.com/stagepalete/ozimiz.git
$ cd ozimiz

Создайте виртуальную среду для установки зависимостей и активируйте ее:

sh
$ python -m venv venv
$ venv\Scripts\activate.bat

Затем установите зависимости:

sh
(env)$ pip install -r requirements.txt
Обратите внимание на (env) перед подсказкой. Это указывает на то, что этот терминал
сеанс работает в виртуальной среде, созданной venv.

Как только pip завершит загрузку зависимостей:
sh
(env)$ python manage.py runserver
И перейдите по адресу http://127.0.0.1:8000/ozimiz/.
```
