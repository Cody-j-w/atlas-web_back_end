-- student bonus procedure



delimiter $$
CREATE PROCEDURE AddBonus(user_id INT, project_name VARCHAR(255), score INT)
    BEGIN
        DECLARE project_id INT;
        SELECT id INTO project_id FROM projects WHERE name = project_name;
        IF project_id IS NULL THEN
            INSERT INTO projects (name)
            VALUES (project_name);
            SET project_id = LAST_INSERT_ID();
        END IF;
        INSERT INTO corrections (score, user_id, project_id)
        VALUES (score, user_id, project_id);

    END;
$$
delimiter ;