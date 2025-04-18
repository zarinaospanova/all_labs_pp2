"""
1 task Функция для поиска по шаблону

CREATE OR REPLACE FUNCTION search_phonebook(pattern TEXT)
RETURNS TABLE(user_id INT, username TEXT, phone_number TEXT) AS $$
BEGIN
    RETURN QUERY
    SELECT * FROM phonebook1 
    WHERE username ILIKE '%' || pattern || '%' 
       OR phone_number ILIKE '%' || pattern || '%';
END;
$$ LANGUAGE plpgsql;

2 task Процедура: вставка пользователя или обновление, если существует

CREATE OR REPLACE PROCEDURE insert_or_update_user(username TEXT, phone TEXT)
LANGUAGE plpgsql
AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM phonebook1 WHERE username = insert_or_update_user.username) THEN
        UPDATE phonebook1 
        SET phone_number = insert_or_update_user.phone 
        WHERE username = insert_or_update_user.username;
    ELSE
        INSERT INTO phonebook1 (username, phone_number) 
        VALUES (insert_or_update_user.username, insert_or_update_user.phone);
    END IF;
END;
$$;

3 task Процедура: массовая вставка и возврат некорректных телефонов

CREATE OR REPLACE PROCEDURE insert_many_users(usernames TEXT[], phones TEXT[], OUT bad_data TEXT[])
LANGUAGE plpgsql
AS $$
DECLARE
    i INT := 1;
BEGIN
    bad_data := '{}';
    WHILE i <= array_length(usernames, 1) LOOP
        IF phones[i] ~ '^\+?[0-9]{10,15}$' THEN
            CALL insert_or_update_user(usernames[i], phones[i]);
        ELSE
            bad_data := array_append(bad_data, usernames[i] || ':' || phones[i]);
        END IF;
        i := i + 1;
    END LOOP;
END;
$$;


4 task Функция: постраничный вывод с limit и offset

CREATE OR REPLACE FUNCTION get_paginated_users(limit_count INT, offset_count INT)
RETURNS TABLE(user_id INT, username TEXT, phone_number TEXT) AS $$
BEGIN
    RETURN QUERY
    SELECT * FROM phonebook1 
    ORDER BY user_id
    LIMIT limit_count OFFSET offset_count;
END;
$$ LANGUAGE plpgsql;


5 task  Процедура удаления по имени или номеру

CREATE OR REPLACE PROCEDURE delete_by_username_or_phone(name_or_phone TEXT)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM phonebook1 
    WHERE username = name_or_phone OR phone_number = name_or_phone;
END;
$$;
"""