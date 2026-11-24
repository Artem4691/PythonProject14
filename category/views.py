from django.shortcuts import render
from django.http.response import HttpResponse, Http404

def hello_world(request):
    return HttpResponse("<h1><a>Hello world!</a></h1>")

def button(request):
    return HttpResponse("""<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Магазин — Категории</title>
    <style>
        /* Базовые настройки страницы и шрифтов */
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #f4f6f9;
            color: #333333;
            line-height: 1.6;
            margin: 0;
            padding: 40px 20px;
        }

        /* Контейнер по центру экрана */
        .container {
            max-width: 800px;
            margin: 0 auto;
            background-color: #ffffff;
            padding: 35px 40px;
            border-radius: 12px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.06);
        }

        /* Стили для заголовков */
        h1 {
            color: #1e293b;
            font-size: 28px;
            margin-top: 0;
            border-bottom: 2px solid #e2e8f0;
            padding-bottom: 12px;
        }

        h2 {
            color: #2563eb;
            font-size: 20px;
            margin-top: 28px;
            margin-bottom: 10px;
        }

        /* Стили для обычного текста и акцентов */
        p {
            font-size: 16px;
            color: #475569;
            margin-bottom: 16px;
        }

        .badge {
            display: inline-block;
            background-color: #dbeafe;
            color: #1d4ed8;
            font-size: 13px;
            font-weight: 600;
            padding: 4px 10px;
            border-radius: 6px;
            margin-bottom: 10px;
        }

        /* Блок-цитата / заметка */
        .note {
            background-color: #f8fafc;
            border-left: 4px solid #2563eb;
            padding: 12px 18px;
            margin: 20px 0;
            font-style: italic;
            color: #334155;
        }

        /* Стили для списка */
        ul {
            padding-left: 20px;
            color: #475569;
        }

        li {
            margin-bottom: 8px;
        }

        /* Кнопка-ссылка */
        .btn {
            display: inline-block;
            margin-top: 15px;
            padding: 10px 20px;
            background-color: #2563eb;
            color: #ffffff;
            text-decoration: none;
            border-radius: 6px;
            font-weight: 500;
        }

        .btn:hover {
            background-color: #1d4ed8;
        }
    </style>
</head>
<body>

    <div class="container">
        <span class="badge">Backend Project • Django</span>
        <h1>Добро пожаловать в каталог</h1>
        
        <p>
            Это тестовая страница для проверки работы маршрутов и представлений. 
            Здесь аккуратно оформлена типографика: настроен межстрочный интервал, 
            цветовые акценты и отступы между блоками.
        </p>

        <div class="note">
            Подсказка: позже сюда можно легко подставить теги шаблонизатора Django, 
            например <strong>{{ category.name }}</strong>.
        </div>

        <h2>Доступные разделы</h2>
        <ul>
            <li><strong>Электроника</strong> — смартфоны, ноутбуки и аксессуары.</li>
            <li><strong>Одежда</strong> — повседневные и спортивные коллекции.</li>
            <li><strong>Книги</strong> — техническая литература по Python и Django.</li>
        </ul>

        <a href="#" class="btn">Перейти к товарам</a>
    </div>

</body>
</html>
""")


def products(request):
    return HttpResponse("""<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Товары</title>
    <style>
        body {
            font-family: 'Segoe UI', sans-serif;
            background-color: #f4f6f9;
            padding: 40px 20px;
            color: #333;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            background: #fff;
            padding: 35px 40px;
            border-radius: 12px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.06);
        }
        h1 { color: #1e293b; border-bottom: 2px solid #e2e8f0; padding-bottom: 12px; }
        .btn {
            display: inline-block;
            margin-top: 15px;
            padding: 10px 20px;
            background-color: #2563eb;
            color: #fff;
            text-decoration: none;
            border-radius: 6px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Список товаров</h1>
        <p>Здесь скоро появятся товары из базы данных Django!</p>
        <a href="/button/" class="btn">← Вернуться в каталог</a>
    </div>
</body>
</html>""")
