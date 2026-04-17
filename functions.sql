CREATE OR REPLACE FUNCTION search_contacts(p_pattern TEXT)
RETURNS TABLE(id INT, name VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY SELECT c.id, c.name, c.phone FROM contacts c
    WHERE c.name ILIKE '%' || p_pattern || '%' OR c.phone ILIKE '%' || p_pattern || '%';
END; $$ LANGUAGE plpgsql;