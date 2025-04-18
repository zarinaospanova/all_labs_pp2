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
