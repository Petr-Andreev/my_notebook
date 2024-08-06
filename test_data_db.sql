INSERT INTO tasks (user_id, title, priority, date_to, completed) VALUES
(1, 'Покормить кота'),
(1, 'Почистить зубы', 'low'),
(2, 'Накраситься', 'low'),
(2, 'Подать документы на отпуск', 'high'),
(3, 'Провести митинг', 'low'),
(3, 'Пообедать'),
(3, 'Собрать статистику работы сотрудников', 'low');

INSERT INTO subtasks (task_id, title, priority, completed) VALUES
(1, 'Купить корм', 'high'),
(1, 'Наложить корм в миску'),
(3, 'Выбрать цвет', 'low'),
(4, 'Заполнить документ', 'high'),
(4, 'Отправить документы на согласование', 'high'),
(5, 'Созвониться с коллегами'),
(6, 'Купить еды в магазине', 'high'),
(7, "Опросить каждого работника"),
(7, "Отфильтровать данные"),
(7, "Составить отчет", 'high');


INSERT INTO users (first_name, last_name, email, hashed_password, role) VALUES
('Petr', 'Andreev', 'pvandreev@ya.ru', 'tut_budet_hashed_password_1', 'admin'),
('Polina', 'Andreeva', 'paandreeva@ya.ru', 'tut_budet_hashed_password_2', 'user'),
('Andrey', 'Andreev', 'avandreev@ya.ru', 'tut_budet_hashed_password_3');
