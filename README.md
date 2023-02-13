# Яндекс афиша

### Описание

Проект - сайт для создания гео-точек с фотографиями и описанием:

[https://yandex-map-where-to-go.ru/](https://axxel123.pythonanywhere.com/)

<img width="781" alt="image" src="https://user-images.githubusercontent.com/58893102/194596161-8b56ce6e-f110-412d-9584-4251f686e551.png">

### Как запустить
- Скачайте код
- Применение миграции

  >python manage.py migrate

- Запустите веб-сервер

  >python manage.py runserver

- Откройте в браузере ссылку (пример на рисунке):

  ![image](https://user-images.githubusercontent.com/58893102/218447613-9a58db02-d718-4bf4-8d18-ceb4bb2ee908.png)


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

### Необходимые файлы

В директории, где находятся **settings.py** создайте файл **.env** .
В него разместите:
- свой SECRET_KEY
- DEBUG=False





