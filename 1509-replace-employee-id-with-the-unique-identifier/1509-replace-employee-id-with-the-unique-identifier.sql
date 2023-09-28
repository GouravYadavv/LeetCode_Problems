select eu.unique_id,e.name
from employeeUNI as eu
right join employees as e
on eu.id=e.id