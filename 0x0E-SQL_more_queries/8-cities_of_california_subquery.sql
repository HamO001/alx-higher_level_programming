-- lists all cities of California that can be found in database hbtn_0d_usa.
-- Results must be sorted in ascending order by cities.id
-- You are not allowed to use the JOIN keyword
-- The database name will be passed as an argument of the mysql command

SELECT `id`, `name` FROM `cities`
WHERE `state_id` IN (
    SELECT `id` FROM `states`
    WHERE `name` = "California"
)
ORDER BY `id`;
