select
	customer_key
	, full_name
	, date_of_birth
	, extract(year from age('{report_date}', date_of_birth)) as age
	, marital_status
	, gender
	, yearly_income
	, number_of_children
	, occupation
	, house_owner_flag
	, number_cars_owned
	, first_purchase_date
	, extract(year from age('{report_date}', first_purchase_date)) as duration
from customers