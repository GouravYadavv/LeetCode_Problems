# Write your MySQL query statement below
select (t.project_id),round(avg(t.experience_years),2) as average_years
from
(
select a.project_id,b.experience_years
from Project as a
left join Employee as b
on a.employee_id=b.employee_id
) as t
group by t.project_id