# Яндекс афиша

### Описание

Проект - сайт для создания гео-точек с фотографиями и описанием:

[https://yandex-map-where-to-go.ru/](https://axxel123.pythonanywhere.com/)

<img width="781" alt="image" src="https://user-images.githubusercontent.com/58893102/194596161-8b56ce6e-f110-412d-9584-4251f686e551.png">

### Как запустить
- Скачайте код
- Перейдите в каталог проекта с файлом index.html
- Запустите веб-сервер
- Откройте в браузере

В качестве веб-сервера можно использовать что угодно. Например, подойдёт даже самый простой встроенный в Python веб-сервер:

>$ python -m http.server 8000

### Настройки
Внизу справа на странице можно включить отладочный режим логгирования.

<img width="177" alt="image" src="https://user-images.githubusercontent.com/58893102/194594930-09a736a1-63d4-4157-9f24-ac158668e2c5.png">

Настройки сохраняются в Local Storage браузера и не пропадают после обновления страницы. Чтобы сбросить настройки удалите ключи из Local Storage с помощью Chrome Dev Tools —> Вкладка Application —> Local Storage.

Если что-то работает не так, как ожидалось, то начните с включения отладочного режима логгирования.


### Источники данных

Фронтенд получает данные из двух источников. Первый источник — это JSON, запечённый внутрь HTML. Он содержит полный список объектов на карте. И он прячется внутри тега >script:

### Используемые библиотеки

* [Leaflet](https://leafletjs.com/) — отрисовка карты
* [loglevel](https://www.npmjs.com/package/loglevel) для логгирования
* [Bootstrap](https://getbootstrap.com/) — CSS библиотека
* [Vue.js](https://ru.vuejs.org/) — реактивные шаблоны на фронтенде






