# RetailCRM-FastAPI-Service

## Запуск

1. Создайте файл `.env` в директории `app` по примеру `.env.template`.

2. Перейдите в директорию, где находится `docker-compose.yml`, и выполните команду:

```bash
docker compose up --build
```

3. После запуска API можно протестировать через Swagger UI по ссылке:

```
http://localhost:8000/docs
```

## Доступные эндпоинты

### Клиенты

- `GET /api/customers` — получить список клиентов (поддерживаются фильтры)
- `POST /api/customers` — создать нового клиента

### Заказы

- `GET /api/orders/` — получить список заказов по ID клиента
- `POST /api/orders/` — создать заказ
- `POST /api/orders/payments/create` — создать платеж
