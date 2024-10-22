# Проект: Погодный скрипт на Python3

Описание:
Данный проект представляет собой программу на Python3, которая выводит информацию о погоде в трех городах: Лондоне, Череповце и Шереметьево. Скрипт может быть использован как внешний модуль в других проектах, так и как самостоятельная программа для получения актуальных данных о погоде.

Функциональные возможности:
- Получение текущей погоды в Лондоне, Череповце и Шереметьево.
- Вывод данных о температуре, влажности и состоянии погоды.
- Поддержка работы как модуля, так и исполняемого скрипта.

Установка:
1. Клонируйте репозиторий:
    git clone <URL_репозитория>
    cd <название_папки>
2. Установите зависимости:
    Убедитесь, что у вас установлен pip, затем выполните:
    ```python
    pip install -r req.txt
    ``` 

Использование:
- Как самостоятельная программа:
    После установки зависимостей просто выполните:
    ```python
    python weather.py
    ``` 
- Как модуль:
    Вы можете импортировать скрипт в своем проекте следующим образом:

```python
from weather import main
main()
``` 
    
Зависимости:
Все необходимые зависимости хранятся в файле req.txt. Убедитесь, что все библиотеки установлены перед использованием программы.
