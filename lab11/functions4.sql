CREATE OR REPLACE FUNCTION get_paginated_users(limit_count INT, offset_count INT)
RETURNS TABLE(user_id INT, username TEXT, phone_number TEXT) AS $$
BEGIN
    RETURN QUERY
    SELECT * FROM phonebook1 
    ORDER BY user_id
    LIMIT limit_count OFFSET offset_count;
END;
$$ LANGUAGE plpgsql;
