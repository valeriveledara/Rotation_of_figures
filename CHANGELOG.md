# Changelog
Все заметные изменения в этом проекте будут задокументированы в этом файле.

Формат основан на [Ведении журнала изменений](https://keepachangelog.com/en/1.0.0/),
и этот проект придерживается [Cемантического Управления Версиями](https://semver.org/spec/v2.0.0.html).
## [0.0.1] - 2023-11-17

### Добавлено

- Реализация отрисовки тетраэдра и конуса в окне OpenGL.
- Возможность вращения сцены с помощью клавиш управления.
- Отображение смешанного цвета с прозрачностью для тетраэдра и конуса.
- Реализован файл README.md с описанием проекта и инструкциями.
- Unit-тесты для функций draw_cone() и draw_tetrahedron(), проверяющие корректность отображения конуса и тетраэдра соответственно.

### Изменено

- Улучшена логика отрисовки конуса для визуальной точности и плавности граней.
- Уточнены комментарии в коде для лучшего понимания работы функций.
