from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey

from app.database import Base


class Tasks(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(ForeignKey('users.id'), nullable=False)  # Столбец внешнего ключа
    title = Column(String, nullable=False)
    priority = Column(String, default="medium")
    date_to = Column(DateTime)
    completed = Column(Boolean, default=False)


class SubTasks(Base):
    __tablename__ = 'subtasks'

    id = Column(Integer, primary_key=True, nullable=False)
    task_id = Column(ForeignKey('tasks.id'), nullable=False)  # Столбец внешнего ключа
    title = Column(String, nullable=False)
    completed = Column(Boolean, default=False)
