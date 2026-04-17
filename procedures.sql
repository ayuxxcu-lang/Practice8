-- 1. Upsert процедурасы
CREATE OR REPLACE PROCEDURE upsert_contact(p_name VARCHAR, p_phone VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM contacts WHERE name = p_name) THEN
        UPDATE contacts SET phone = p_phone WHERE name = p_name;
    ELSE
        INSERT INTO contacts(name, phone) VALUES(p_name, p_phone);
    END IF;
END; $$;

-- 2. Өшіру процедурасы
CREATE OR REPLACE PROCEDURE delete_contact(p_search TEXT)
LANGUAGE plpgsql AS $$
BEGIN
    DELETE FROM contacts WHERE name = p_search OR phone = p_search;
END; $$;

-- 3. Көптеп қосу процедурасы (тексерумен)
CREATE OR REPLACE PROCEDURE insert_many_contacts(p_names VARCHAR[], p_phones VARCHAR[])
LANGUAGE plpgsql AS $$
DECLARE i INT;
BEGIN
    FOR i IN 1..array_length(p_names, 1) LOOP
        IF LENGTH(p_phones[i]) >= 5 THEN -- нөмір ұзындығын тексеру
            INSERT INTO contacts(name, phone) VALUES(p_names[i], p_phones[i])
            ON CONFLICT (phone) DO NOTHING;
        END IF;
    END LOOP;
END; $$;