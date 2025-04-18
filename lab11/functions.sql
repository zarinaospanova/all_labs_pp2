CREATE OR REPLACE FUNCTION search_phonebook(pattern TEXT)
RETURNS TABLE(user_id INT, username TEXT, phone_number TEXT) AS $$
BEGIN
    RETURN QUERY
    SELECT * FROM phonebook1 
    WHERE username ILIKE '%' || pattern || '%' 
       OR phone_number ILIKE '%' || pattern || '%';
END;
$$ LANGUAGE plpgsql;

