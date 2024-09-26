# Write your MySQL query statement below
WITH ranked_courses AS (
    SELECT 
        student_id, 
        course_id, 
        grade,
        ROW_NUMBER() OVER (PARTITION BY student_id ORDER BY grade DESC, course_id ASC) AS rank_col
    FROM Enrollments
)
SELECT student_id, course_id, grade
FROM ranked_courses
WHERE rank_col = 1
ORDER BY student_id;


