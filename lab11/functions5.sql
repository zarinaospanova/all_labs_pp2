CREATE OR REPLACE PROCEDURE delete_by_username_or_phone(name_or_phone TEXT)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM phonebook1 
    WHERE username = name_or_phone OR phone_number = name_or_phone;
END;
$$;
