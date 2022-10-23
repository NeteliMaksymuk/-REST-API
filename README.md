# REST-API

Перейти в папку проекту
Створити віртуальне середовище за допомогою venv:
> python3 -m venv env

Активувати віртуальне середовище
> source ./env/bin/activate

Завантажити залежності
>pip install -r requirements.txt

Далі потрібно збілдити image командою:
>  docker build --build-arg PORT=<your port> . -t <image_name>:latest

Далі запустити контейнер за допомогою команд:
> docker-compose build
>
> docker-compose up
