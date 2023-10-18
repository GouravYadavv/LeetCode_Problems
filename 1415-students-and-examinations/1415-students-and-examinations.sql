/* Write your T-SQL query statement below */

with cte as
(select * from students
cross join subjects) 

select c.student_id,c.student_name,c.subject_name,sum(case when e.subject_name is null then 0 else 1 end) as attended_exams
from cte c
left join examinations e
on c.student_id=e.student_id and c.subject_name=e.subject_name
group by c.student_id,c.student_name,c.subject_name