# Лабораторная работа №5 по дисциплине "Компьютерная графика"

[![License: MIT ](https://img.shields.io/badge/License-MIT-red.svg)](https://opensource.org/licenses/MIT)
![Python](https://img.shields.io/badge/Python-3.11.1-green)
[![Build and Test](https://github.com/valeriveledara/Rotation_of_figures/actions/workflows/ci.yml/badge.svg)](https://github.com/valeriveledara/Rotation_of_figures/actions/workflows/ci.yml)
[![Version](https://img.shields.io/badge/release-v0.0.1-darkblue.svg)](https://github.com/valeriveledara/Rotation_of_figures/releases/tag/v0.0.1)
[![Telegram](https://img.shields.io/badge/Telegram-bloody_marr-22A5E0?style=social&logo=telegram)](https://t.me/bloody_marr)

## Описание задачи
> Требуется составить программу, отображающую пересечение тетраэдра и цилиндра. Необходимо предусмотреть возможность поворота тела вокруг основных осей.

## Демонстрация выполнения работы программы
<img src = "GIF/animation.gif">

## Используемые библотеки и наборы инструментов
- OpenGL.GL и OpenGL.GLU - для работы с графическими возможностями OpenGL, включая отрисовку трехмерных объектов и взаимодействие с графической библиотекой Pygame.
- glfw для создания окон с контекстом OpenGL и обработки событий ввода; предоставляет минимальный набор функций, необходимых для создания графического приложения с использованием OpenGL.

## Установка, запуск и тестирование
1. Клонируйте репозиторий
``` 
   git clone https://github.com/valeriveledara/Rotation_of_figures.git
```
2. Перейдите в директорию проекта
``` 
    cd <Rotation_of_figures-master>
```
3. Установите зависимости
```
pip install -r requirements.txt
```
4. Откройте терминал в папке проекта и выполните следующую компанду
```
   python main.py
```
5. Для запуска тестов используйте команду
```
   python -m unittest discover tests
```
## Инструкция по использованию
После запуска программы Вы можете вращать объект, изображенный на экране, с помощью клавиш со стрелками на клавиатуре.
- Стрелка влево: Вращение объекта против часовой стрелки вокруг вертикальной оси.
- Стрелка вправо: Вращение объекта по часовой стрелке вокруг вертикальной оси.
- Стрелка вверх: Вращение объекта вперед вокруг горизонтальной оси.
- Стрелка вниз: Вращение объекта назад вокруг горизонтальной оси.


## Лицензия
Этот проект лицензирован в соответствии с условиями лицензии [MIT](LICENSE).
