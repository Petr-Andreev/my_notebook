INSERT INTO tasks (user_id, title, priority, date_to, completed) VALUES
(1, 'Покормить кота', DEFAULT, DEFAULT, FALSE),
(1, 'Почистить зубы', 'low', DEFAULT, DEFAULT),
(2, 'Накраситься', 'low', DEFAULT, DEFAULT),
(2, 'Подать документы на отпуск', 'high', DEFAULT, DEFAULT),
(3, 'Провести митинг', 'low', DEFAULT, DEFAULT),
(3, 'Пообедать', 'high', DEFAULT, DEFAULT),
(3, 'Собрать статистику работы сотрудников', 'low', DEFAULT, DEFAULT);

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
