from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey
from datetime import datetime, timedelta
from app.database import Base

def default_tomorrow():
    return datetime.utcnow().date() + timedelta(days=1)  # Возвращаем завтрашнюю дату

class Tasks(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(ForeignKey('users.id'), nullable=False)  # Столбец внешнего ключа
    title = Column(String, nullable=False)
    priority = Column(String, default="medium")
    date_to = Column(Date, default=default_tomorrow)  # Устанавливаем значение по умолчанию на завтрашнюю дату
    completed = Column(Boolean, default=False)


class SubTasks(Base):
    __tablename__ = 'subtasks'

    id = Column(Integer, primary_key=True, nullable=False)
    task_id = Column(ForeignKey('tasks.id'), nullable=False)  # Столбец внешнего ключа
    title = Column(String, nullable=False)
    priority = Column(String, default="medium")
    completed = Column(Boolean, default=False)
