# Асинхронный парсер сайта [https://peps.python.org/](https://peps.python.org/). Собирает информацию о всех PEP и сохраняет их в папке `/results/`:

## Находясь в папке `SCRAPY_PARSER_PEP` необходимо:
### Развернуть виртуальное окружение
```sh
python -m venv venv
```
### Активировать виртуальное окружение
```sh
source venv/Scripts/activate
```
### Установить зависимости
```sh
pip install -r requirements.txt
```
### Запустить парсер Scrapy
```sh
scrapy crawl pep
```

## В результате в папке `results` получим два .`csv` файла:

## Файл "pep_\<datetime>.csv" содержит номер PEP, его название и статус.

### 3 колонки - `number` `name` `status`

## Файл "status_summary_\<datetime>.csv" содержит статистику о всех PEP, а именно статус PEP + количество PEP с данным статусом. Так же содержит общее количество PEP.

### 2 колонки - `Статус` `Количество`

## Стек
  * Python
  * Scrapy
  * CSV

### GitHub [avdeevdmitrykrsk](https://github.com/avdeevdmitrykrsk)
