-- Write your query below
select name from customers where id not in 

(select c.id from customers c
join 
orders o on o.customer_id=c.id);