from fastapi import FastAPI

from .api import router


tags_metadata = [
    {
        'name': 'auth',
        'description': 'Авторизация и регистрация',
    },
    {
        'name': 'operations',
        'description': 'Создание, редактирование, удаление и просмотр операций',
    },
    {
        'name': 'reports',
        'description': 'Импорт и экспорт CSV-отчетов',
    },
]

app = FastAPI(
    title='WORKSHOP API',
    description='Первый опыт создания API',
    version='1.0',
    openapi_tags=tags_metadata,
)
app.include_router(router)
