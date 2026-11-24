INSERT INTO positions (group_id, name)
SELECT id, 'Тестовый программист'
FROM position_groups WHERE name = 'IT отдел';

INSERT INTO positions (group_id, name)
SELECT id, 'Тестовый системный администратор'
FROM position_groups WHERE name = 'IT отдел';

INSERT INTO positions (group_id, name)
SELECT id, 'Тестовый бухгалтер'
FROM position_groups WHERE name = 'Бухгалтерия';

INSERT INTO employees (last_name, first_name, middle_name, birth_date, position_id)
SELECT 'Иванов', 'Иван', 'Иванович', DATE '1995-05-14', id
FROM positions WHERE name = 'Тестовый программист';

INSERT INTO employees (last_name, first_name, middle_name, birth_date, position_id)
SELECT 'Петрова', 'Анна', 'Сергеевна', DATE '1998-09-21', id
FROM positions WHERE name = 'Тестовый системный администратор';

INSERT INTO employees (last_name, first_name, middle_name, birth_date, position_id)
SELECT 'Сидоров', 'Павел', NULL, DATE '1990-02-10', id
FROM positions WHERE name = 'Тестовый бухгалтер';

COMMIT;