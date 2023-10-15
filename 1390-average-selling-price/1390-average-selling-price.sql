# Write your MySQL query statement below

select a.product_id,
ifnull(round(sum(units*price*1.0)/sum(units),2),0) as 
average_price

from Prices a
left join UnitsSold b
on a.product_id=b.product_id
and b.purchase_date>=a.start_date and b.purchase_date<=a.end_date
group by a.product_id