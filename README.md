# Dog Breed API - Документация

## О проекте

Dog Breed API - это RESTful веб-сервис для управления информацией о собаках и их породах. API предоставляет CRUD-функциональность для работы с данными о собаках и их породах.

## Стек технологий

- Python 3.9
- Django 4.2
- Django REST Framework 3.14
- PostgreSQL 13
- Docker

## Установка и запуск

### 1. Требования

- Docker и Docker Compose
- Python 3.9+ (если запускаете без Docker)

### 2. Установка с Docker

```bash
# Клонировать репозиторий
git clone https://github.com/your-repo/dog-breed-api.git
cd practice_3

# Создать файл .env на основе примера
cp .env.example .env

# Запустить сервисы
docker-compose up -d --build
```

### 3. Установка без Docker

```bash
# Установить зависимости
pip install -r requirements.txt

# Настроить базу данных PostgreSQL
# Создать файл .env и указать параметры подключения

# Применить миграции
python manage.py migrate

# Запустить сервер
python manage.py runserver
```

## Архитектура проекта

### Основные компоненты

1. **Модели**:
   - `Breed` - породы собак
   - `Dog` - собаки

2. **API Endpoints**:
   - `/api/breeds/` - управление породами
   - `/api/dogs/` - управление собаками

3. **Сериализаторы**:
   - `BreedSerializer` - для списка пород
   - `BreedDetailSerializer` - для детальной информации о породе
   - `DogSerializer` - для списка собак
   - `DogDetailSerializer` - для детальной информации о собаке

4. **ViewSets**:
   - `BreedViewSet` - обработка запросов для пород
   - `DogViewSet` - обработка запросов для собак

## Примеры использования API

### 1. Работа с породами

**Создание породы**:
```bash
POST /api/breeds/
{
    "name": "Labrador",
    "size": "Large",
    "friendliness": 5,
    "trainability": 4,
    "shedding_amount": 3,
    "exercise_needs": 4
}
```

**Получение списка пород**:
```bash
GET /api/breeds/
```
Ответ включает информацию о породах, а также количество собак каждой породы.

### 2. Работа с собаками

**Добавление собаки**:
```bash
POST /api/dogs/
{
    "name": "Max",
    "age": 3,
    "breed": 1,
    "gender": "Male",
    "color": "Black",
    "favorite_food": "Chicken",
    "favorite_toy": "Ball"
}
```

**Получение информации о собаках**:
```bash
GET /api/dogs/
```
Ответ включает основную информацию о собаках и средний возраст собак определенной породы

**Получение информации о собаке**:
```bash
GET /api/dogs/1/
```
Ответ включает:
- Информацию о собаке
- Основные данные о породе
- Количество собак той же породы