-- Script to create a procedure
-- Create procedure computed average weighted score
DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    -- Declare variables
    DECLARE done INT DEFAULT FALSE;
    DECLARE user_id INT;
    DECLARE avg_weighted_score FLOAT;
    DECLARE total_weight FLOAT;
    DECLARE total_weighted_score FLOAT;
    
    -- Declare a cursor to iterate over each user
    DECLARE user_cursor CURSOR FOR
        SELECT id FROM users;
        
    -- Declare a continue handler for the cursor
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    -- Open the cursor
    OPEN user_cursor;
    
    -- Loop through each user
    read_loop: LOOP
        FETCH user_cursor INTO user_id;
        IF done THEN
            LEAVE read_loop;
        END IF;

        -- Initialize total weight and total weighted score
        SET total_weight = 0;
        SET total_weighted_score = 0;
        
        -- Calculate the total weighted score and total weight for the current user
        SELECT SUM(c.score * p.weight) INTO total_weighted_score
        FROM corrections c
        JOIN projects p ON c.project_id = p.id
        WHERE c.user_id = user_id;

        SELECT SUM(p.weight) INTO total_weight
        FROM corrections c
        JOIN projects p ON c.project_id = p.id
        WHERE c.user_id = user_id;

        -- Avoid division by zero
        IF total_weight = 0 THEN
            SET avg_weighted_score = 0;
        ELSE
            -- Compute the average weighted score
            SET avg_weighted_score = total_weighted_score / total_weight;
        END IF;

        -- Update the average_score in the users table
        UPDATE users
        SET average_score = avg_weighted_score
        WHERE id = user_id;
    END LOOP;
    
    -- Close the cursor
    CLOSE user_cursor;
END$$

DELIMITER ;
