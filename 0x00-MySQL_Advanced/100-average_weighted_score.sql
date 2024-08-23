-- Script to create stored procedure
-- create stored procedure compute average weighted score
DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
    DECLARE avg_weighted_score FLOAT;
    DECLARE total_weight FLOAT;
    DECLARE total_weighted_score FLOAT;

    -- Initialize total weight and total weighted score
    SET total_weight = 0;
    SET total_weighted_score = 0;

    -- Calculate the total weighted score and total weight
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
END$$

DELIMITER ;

