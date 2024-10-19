# Write your MySQL query statement below
SELECT   
    t.team_id,  
    t.team_name,  
    COALESCE(SUM(CASE   
        WHEN m.host_team = t.team_id AND m.host_goals > m.guest_goals THEN 3  
        WHEN m.host_team = t.team_id AND m.host_goals = m.guest_goals THEN 1   
        ELSE 0   
    END), 0) +   
    COALESCE(SUM(CASE   
        WHEN m.guest_team = t.team_id AND m.guest_goals > m.host_goals THEN 3  
        WHEN m.guest_team = t.team_id AND m.guest_goals = m.host_goals THEN 1   
        ELSE 0   
    END), 0) AS num_points  
FROM   
    Teams t  
LEFT JOIN   
    Matches m ON t.team_id = m.host_team OR t.team_id = m.guest_team  
GROUP BY   
    t.team_id, t.team_name  
ORDER BY   
    num_points DESC,   
    t.team_id ASC;