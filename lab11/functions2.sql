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
