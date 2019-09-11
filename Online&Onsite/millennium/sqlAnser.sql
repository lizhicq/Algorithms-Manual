--- Sql Server ---
--- 1 ---
use test;

CREATE TABLE imag_code_test
(
    ord_status VARCHAR(10),
    ord_id INT,
    ord_original_ord_id INT,
    ord_quantity INT, 
    ord_trader VACHAR(MAX),
    ord_update_date_time TIMESTAMP
)

INSERT INTO imag_code_test active (ord_status, ord_id, ord_original_ord_id, ord_quantity, ord_trader, ord_update_date_time) values ('active', 1200 1200 199 'A' '1/29/2014 5:05')
...
INSERT INTO imag_code_test active (ord_status, ord_id, ord_original_ord_id, ord_quantity, ord_trader, ord_update_date_time) values ('audit' 1294 1288 90 'A' '1/15/2014 5:05')


--- 2 ---

select * from imag_code_test
where order_id = 1288
or ord_original_ord_id = 1288


--- 3 --- 

select * from imag_code_test
where ord_id = ord_original_ord_id
and count(ord_original_ord_id) == count(ord_id)

--- 4 ---
select top 2 ord_trader from imag_code_test
order by ord_quantity
desc

--- 5 --- 
select ord_id from imag_code_test t1 
where (select (t1.ord_quantity*t2.ord_quantity) 
from imag_code_test  t2 
where t2.order_id=t1.order_id)<0

--- 6 --- 
select ord_id from imag_code_test t1 
where (select abs(t1.ord_update_date_time - t2.ord_update_date_time) 
from imag_code_test  t2 
where t2.order_id=t1.order_id)< 1




