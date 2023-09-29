# Write your MySQL query statement below
select e.name as employee

from employee as e

inner join employee as b

on e.managerId=b.id

where e.salary>b.salary