
Установка зависимостей
```bash
pip install -r requirements.txt
```
Инициализирование базы данных
```python
from workshop.database import engine
from workshop.tables import Base

Base.metadata.create_all(engine)
```
Запуск
```bash
python -m src.workshop
```